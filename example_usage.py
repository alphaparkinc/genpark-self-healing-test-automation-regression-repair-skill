from client import SelfHealingTestAutomationRegressionRepairClient

def main():
    client = SelfHealingTestAutomationRegressionRepairClient()
    res = client.repair_failing_tests('tests/ui/login.spec.ts', 'TimeoutError: locator button#submit-btn not found')
    print('Suite: ' + res['test_suite'] + ' | Healed: ' + str(res['tests_healed_count']) + ' | Pass Rate: ' + str(res['retest_pass_rate_pct']) + '%')
    print('PR: ' + res['pr_draft_created'])
    for r in res['repaired_tests']:
        print('  [' + r['test_case'] + '] ' + r['old_selector'] + ' -> ' + r['repaired_selector'] + ' (' + str(r['confidence_pct']) + '% confidence)')

if __name__ == '__main__':
    main()
