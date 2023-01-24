from pages.base_page import BasePage


class AddPlayer(BasePage):
    player_name_field_xpath = "//input[@name='name']"
    player_surname_field_xpath = "//input[@name='surname']"
    player_age_field_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[@data-value='right']"
    left_leg_xpath = "//li[@data-value='left']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']/span[1]"
    edit_player_header_xpath = "//span[contains(@class, 'MuiTypography-h5')]"
    pass