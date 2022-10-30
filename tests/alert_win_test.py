from time import sleep

from pages.alert_win_page import NewTabPage, AlertPage, FramePage


class TestAlertTabWin:
    class TestNewTab:
        def test_new_tab(self, driver):
            new_tab_page = NewTabPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_open_new_tab()
            assert text_result == 'This is a sample page', 'что то пошло не так'



        def test_new_win(self, driver):
            new_win_page = NewTabPage(driver, 'https://demoqa.com/browser-windows')

            new_win_page.open()
            text_result = new_win_page.check_open_new_win()
            assert text_result == 'This is a sample page', 'что то пошло не так'


        def test_new_mess(self, driver):
            new_mess_page = NewTabPage(driver, 'https://demoqa.com/browser-windows')

            new_mess_page.open()
            text_result = new_mess_page.check_open_new_mess()


            # assert text_result == '"Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."', 'что то пошло не так'
            print(text_result)


    class TestAlert:

        def test_alert1(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert1 = alert_page.check_alert1()
            assert alert1 == 'You clicked a button'


        def test_alert2(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert2 = alert_page.check_alert2()
            assert alert2 == 'This alert appeared after 5 seconds'


        def test_alert3(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert3 = alert_page.check_alert3()
            assert alert3 == 'You selected Ok'

        def test_alert4(self, driver):
            alert_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert4 = alert_page.check_alert4()
            # print(text, alert4)
            assert alert4 == f'You entered {text}'
            # assert text in alert4

    class TestFrame:
        def test_frame(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result1 = frame_page.check_frame('frame1')
            result2 = frame_page.check_frame('frame2')
            assert result1 == ['This is a sample page', '500px', '350px']
            assert result2 == ['This is a sample page', '100px', '100px']


