#!/usr/bin/env python3
"""Finite V11–V18 PR status and dependency audit: conservative per PR.

Statuses are evidence classifications for research, NOT merge approvals.
Derived from the GitHub PR snapshots, local native tests and existing
artifact validators; does not call GitHub or GitHub Actions.
"""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MAP={
 "V11":{"S3":[408],"S3-Benchmarks":[53],"Relat-rio":[69]},
 "V12-A":{"S3":[409],"S3-Benchmarks":[54],"Relat-rio":[70]},
 "V12-B":{"S3":[410],"S3-Benchmarks":[55],"Relat-rio":[71]},
 "V13":{"S3":[411],"S3-Benchmarks":[56],"Relat-rio":[72]},
 "V14":{"S3":[412],"S3-Benchmarks":[57],"Relat-rio":[73]},
 "V15":{"S3":[413],"S3-Benchmarks":[58],"Relat-rio":[74]},
 "V16":{"S3":[414],"S3-Benchmarks":[59],"Relat-rio":[75]},
 "V17":{"S3":[415],"S3-Benchmarks":[60],"Relat-rio":[76]},
 "V18":{"S3":[416],"S3-Benchmarks":[61],"Relat-rio":[77]},
}
ASSESSMENTS={
 "V11":("GO_EXPERIMENTAL_ONLY","Proven cyclic GF2 algorithm selection restricted to source IR; not a general automatic compiler optimization."),
 "V12-A":("GO_EXPERIMENTAL_COMPATIBLE_SUBSET","Separate checked i64 progression and empirical strategy registry; source/IR proof and native tests, not in production pipeline."),
 "V12-B":("GO_EXPERIMENTAL_COMPATIBLE_SUBSET","Independent GF2 and identity candidate registry; opt-in, source-bound proof, composes with V12-A in tested scenarios."),
 "V13":("GO_EXPERIMENTAL_ONLY","Certified CTZ/inline GF2 native specializations, performance wins and known small workload regression; not default."),
 "V14":("NO_GO_GLOBAL_DEFAULT","Selective x86 peephole optimization with mixed performance; needs cost gate and broader ABI/control checks."),
 "V15":("GO_EXPERIMENTAL_ONLY","Local slice bounds reuse proved under strict guards; no universal enablement."),
 "V16":("GO_EXPERIMENTAL_ONLY","Static stencil interval proof, selected observed speedups only; preserve overflow and traps."),
 "V17":("GO_EXPERIMENTAL_ONLY","Dynamic-width stencil intervals under preexisting guard, strict dominance and bounds; no general induction solver."),
 "V18":("GO_EXPERIMENTAL_ONLY","Synthesized guarded cloned loop, exact native budget/trap tests, 57/63 wins but six regressions and code growth."),
}
GATES={
 "V11":["Proof scope restricted to verified GF2 IR, default integration intentionally off","Select modern integration baseline from 663-commit stack"],
 "V12-A":["Not connected to production compiler; preserve separate opt-in","Physical RX580 dispatch not validated here"],
 "V12-B":["Keep distinct eligibility from V12-A","No default automatic registry promotion"],
 "V13":["Mixed benchmark observations and GPU hardware comparisons","No global CPU/GPU dispatch enablement"],
 "V14":["Mixed x86 codegen gains; global default NO-GO","Requires cost and instruction count rejection heuristics"],
 "V15":["Only marked TSLOAD bounds proof, limited structured cases","Do not make global default before compiler-wide suite"],
 "V16":["Proven static neighbor offsets, not arbitrary dynamic induction","Must keep exact error/overflow parity"],
 "V17":["Source-authored width guard required, no automatic preheader","Keep dominance fail-closed"],
 "V18":["Code-size expansion and six native regressions","Only one WSL host; stronger I-cache/ABI analysis before default"],
}


def read(name):
    return json.loads((ROOT/name).read_text("utf-8-sig"))


def generate():
    inventory=read("pr_stack_20261115.json")
    test=read("release_triage_matrix_20261115.json")
    coexistence=read("v12_coexistence_20261115.json")
    baseline=read("baseline_20261115.json")
    assert test["observed_success"] and test["test_exit_code"]==0
    assert coexistence["all_selected_tests_pass"]
    assert baseline["all_mandatory_gates_passed"]
    assert test["inherited_tests_still_open"]
    all_pr=[]
    for phase,one in MAP.items():
        status,meaning=ASSESSMENTS[phase]
        for repo,ids in one.items():
            candidates={
                x["number"]:x
                for x in inventory["repos"][repo]["selected_prs"]
            }
            for pr_no in ids:
                source=candidates[pr_no]
                # These results are source-code suite evidence, not direct
                # certification of every benchmark or report's content.
                verification=(
                    "SOURCE_IR_NATIVE_SELECTED_TESTS"
                    if repo=="S3"
                    else (
                        "BENCH_ARTIFACT_VALIDATORS_PASS"
                        if repo=="S3-Benchmarks" and phase in {"V15","V16","V17","V18"}
                        else "LINKED_RESEARCH_ONLY_NOT_INDIVIDUALLY_VALIDATED"
                    )
                )
                all_pr.append({
                    "repo":repo,
                    "number":pr_no,
                    "url":source["url"],
                    "title":source["title"],
                    "stage":phase,
                    "head":source["headRefName"],
                    "base":source["baseRefName"],
                    "base_is_open_pr":source["parent_open_pr"],
                    "draft":source["isDraft"],
                    "decision":status,
                    "meaning":meaning,
                    "verification_scope":verification,
                    "source_tests_collected":test["counts_by_stage"][phase],
                    "blocked_for_merge":True,
                    "unmet_gates":GATES[phase],
                })
    assert len(all_pr)==27
    summary={
        "campaign":"S3_CORE_V11_V18_FINITE_PR_TRIAGE",
        "snapshot_date":"2026-11-15",
        "outcome":"TRIAGE_COMPLETE_NO_RELEASE_APPROVAL",
        "source":"PR snapshots on 2026-11-15 + WSL test and selected artifact logs",
        "decisions":all_pr,
        "counts":dict(Counter(item["decision"] for item in all_pr)),
        "all_still_draft":all(x["draft"] for x in all_pr),
        "all_blocked_for_merge":all(x["blocked_for_merge"] for x in all_pr),
        "source_selected_test_count":test["collected_total"],
        "source_regression_result":"PASS_WITH_EXPLICIT_HEREDITARY_DESELECTION",
        "v12_separate_sibling_compatibility":"93 V12 and 159 V18 local test executions passed; overlap in tests allowed",
        "v12_fork_disjoint_files":True,
        "inherited_failures_not_repaired":True,
        "main_to_v18_gap_commits":663,
        "next_action":"KB-0030 repair two inherited fixtures; repeat full local suite with no deselections; choose integration branch only after approval",
        "merges":0,
        "deployments":0,
        "github_actions_used":False,
        "gpu_or_compact_doom_modified":False,
    }
    (ROOT/"pr_decisions_20261115.json").write_text(
        json.dumps(summary,ensure_ascii=False,indent=2)+"\n","utf-8",
    )
    md=[
        "# S3 Core — triagem finita das 27 PRs V11–V18",
        "",
        "**Campanha:** S3_CORE_V11_V18_FINITE_PR_TRIAGE",
        "**Data:** 15/11/2026; verificação local Windows + WSL, sem GitHub Actions.",
        "**Resultado:** matriz de pesquisa concluída; **nenhuma PR aprovada para merge/deploy/default enablement**.",
        "",
        "A main histórica S3 `9b39c707` está 663 commits atrás da candidata `1a323a03`.",
        "O ramo até V18 desce da V12-B, e a V12-A foi aplicada somente em worktrees isoladas.",
        "",
        f"A execução conjunta V11–V18 + V12-A selecionou **{test['collected_total']} testes**",
        "no corpus explícito, com todas as verificações locais passando,",
        "exceto **dois testes herdados previamente conhecidos que foram deselecionados**.",
        "Ambos os testes herdados falharam em execuções independentes; não são PASS.",
        "",
        "Além disso, a coabitação V12-A+B passou 93 testes e a V18+V12-A",
        "passou 159 (252 execuções, incluindo casos repetidos).",
        "",
        "## Decisões individuais",
        "",
        "| Etapa | Repositório | PR | Base | Decisão | Prova disponível |",
        "|---|---|---|---|---|---|",
    ]
    for row in all_pr:
        md.append(
            f"| {row['stage']} | {row['repo']} | [#{row['number']}]({row['url']}) "
            f"| `{row['base']}` | `{row['decision']}` "
            f"| {row['verification_scope']} |"
        )
    md += [
        "",
        "## Matriz de aceitação por camada",
        "",
        "| Etapa | Testes selecionados, incluindo parâmetros | Conclusão |",
        "|---|---:|---|",
    ]
    for name,(status,desc) in ASSESSMENTS.items():
        md.append(f"| {name} | {test['counts_by_stage'][name]} | {status}: {desc} |")
    md += [
        "",
        "## Restrições e caminho de integração",
        "",
        "1. A família V11–V18 continua uma pilha experimental e não é uma release consolidada.",
        "2. V12-A (#409) e V12-B (#410) convivem nos testes, mas são registries distintos",
        "   e não devem ser fundidos pelo simples fato de não haver conflito textual.",
        "3. V13 CTZ mostra casos favoráveis e regressões pequenas; V14 tem ganhos mistos;",
        "   V15–V17 só provam subconjuntos de offsets, guardas e limites;",
        "   V18 cresce o código e sofre seis regressões no estudo publicado.",
        "4. Os dados de benchmark/relatórios mais antigos não foram todos reexecutados",
        "   nesta triagem; seus respectivos campos de verificação estão marcados como tal.",
        "5. **Próximo gate P0:** KB-0030 corrigir fixture FFI `predictive_exact`",
        "   e cobertura dos novos opcodes, depois repetir a matriz local **sem excluir testes**.",
        "6. Após testes limpos, decidir estratégia de integração separadamente,",
        "   respeitando dependências e versão base; nunca fazer merge por série.",
        "7. Compact, DOOM, GPU e produção ficam congelados; nenhum Actions pago ou deploy.",
        "",
        "Evidências: `pr_decisions_20261115.json`, `release_triage_matrix_20261115.json`,",
        "`baseline_20261115.json`, `v12_coexistence_20261115.json` e logs.",
    ]
    (ROOT/"PR_TRIAGE_V11_V18_20261115.md").write_text(
        "\n".join(md)+"\n","utf-8",
    )
    print("TRIAGE",len(all_pr),"PRs; statuses",summary["counts"],flush=True)
    print("SOURCE_TESTS",test["collected_total"],flush=True)
    print("DECISION NO_MERGE_NO_DEPLOY",flush=True)


if __name__=="__main__":generate()
