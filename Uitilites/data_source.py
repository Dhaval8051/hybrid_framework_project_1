#--------------------Data_Source------------------------#


from Uitilites import read_utilites

test_invalid_login_data = [
 ("digital@gmail", "digital123", "Couldn’t find a LinkedIn account associated with this email. Try again or create an account ."),
  ("softwaredev@gmail", "software7654", "Couldn’t find a LinkedIn account associated with this email. Try again or create an account ."),
  ("arduino@gmail", "arduino9987", "Couldn’t find a LinkedIn account associated with this email. Try again or create an account .")
]

# test_add_valid_employee_data = [
#     ["dhavalkhatri8051@gmail.com", "Dhaval@1995", "Rupesh Khatri", "rups125@gmail.com", "Engineer"]]
#
# #test_add_valid_employee_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx", "test_add_valid_employee")
# #test_invalid_profile_upload_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx","test_invalid_profile_upload")
#
#
# test_invalid_login_data = read_utilites.get_csv_as_list("../test_data/test_invalidLogin.csv")