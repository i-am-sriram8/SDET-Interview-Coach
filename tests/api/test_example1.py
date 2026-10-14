"""
    pm.test("Status is 201", () => pm.response.to.have.status(201));

    pm.test("Response time under 1s", () => pm.expect(pm.response.responseTime).to.be.below(1000)):

    const body = pm.response.json();
    pm.test("Case created as open", () => {
        pm.expect(body.status).to.eql("open");
        pm.expect(body.id).to.be.a("number");
    });

    pm.environment.set("case_id", body.id);
"""