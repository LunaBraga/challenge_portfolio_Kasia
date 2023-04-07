from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_text_xpath = "//*[text()='Scouts Panel']"
    main_page_hyperlink - xpath = "//*[contains(@class, 'MuiTypography-root')]"
    players_text_xpath = "//*[text()='Players']"
    english_language_xpath = "//*[text()='English']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    players_count_text_xpath = "//*[text()='Players count']"
    matches
    count_text_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    eventcount_text_xpath = "//*[text()='Events count']"
    add_player_hyperlink_xpath = "//*[text()='Add player']"
pass