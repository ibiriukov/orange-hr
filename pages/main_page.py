# pages/main_page.py
class MainPage:
    def __init__(self, page):
        self.page = page
        self.tabs_in_side_panel = page.locator(".oxd-sidepanel-body ul li")

    def select_tab_in_side_panel(self, tabName):
        for i in range(self.tabs_in_side_panel.count()):
            tab = self.tabs_in_side_panel.nth(i)
            if tab.text_content().strip() == tabName:
                tab.click()
                if tabName == "PIM":
                    from pages.pim_page import PimPage
                    return PimPage(self.page)
                elif tabName == "Leave":
                    from pages.leave_page import LeavePage
                    return LeavePage(self.page)
                elif tabName == "Recruitment":
                    from pages.recruitment_page import RecruitmentPage
                    return RecruitmentPage(self.page)
                # Add more tabs as needed
                return None
        raise ValueError(f"Tab {tabName} not found in side panel")
