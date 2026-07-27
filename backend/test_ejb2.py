import main
code = "import javax.ejb.Stateless;\nimport javax.annotation.Resource;\n@Stateless\npublic class BankService {\n    @EJB\n    private AccountService accountService;\n    @Resource\n    private DataSource ds;\n}"
r = main.migrate_java(code)
print(repr(r.get("migrated_code")))