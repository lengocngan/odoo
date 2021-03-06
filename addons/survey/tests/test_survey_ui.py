import odoo.tests
# Part of Odoo. See LICENSE file for full copyright and licensing details.


@odoo.tests.common.at_install(False)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_admin_survey_tour(self):
        self.phantom_js("/", "odoo.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "odoo.__DEBUG__.services['web.Tour'].tours.test_survey", login="admin")

    def test_02_demo_survey_tour(self):
        self.phantom_js("/", "odoo.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "odoo.__DEBUG__.services['web.Tour'].tours.test_survey", login="demo")

    def test_03_public_survey_tour(self):
        self.phantom_js("/", "odoo.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "odoo.__DEBUG__.services['web.Tour'].tours.test_survey")
