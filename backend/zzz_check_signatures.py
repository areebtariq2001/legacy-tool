import main
import inspect

endpoints_to_check = ['risk_assessment_endpoint', 'map_transaction_flow_endpoint', 'code_quality_endpoint', 'migration_roadmap_endpoint', 'code_smells_endpoint', 'service_boundaries_endpoint', 'migration_roi_endpoint', 'extract_business_rules_endpoint', 'qa_check_endpoint', 'estimate_cost_endpoint']

with open("zzz_signatures.txt", "w") as f:
    for name in dir(main):
        for target in endpoints_to_check:
            if target.replace('_endpoint','') in name.lower().replace('-','_') and 'endpoint' in name.lower():
                try:
                    sig = inspect.signature(getattr(main, name))
                    f.write(name + str(sig) + "\n")
                except:
                    pass

print("DONE")