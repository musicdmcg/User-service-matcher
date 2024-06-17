Changelog
v0.4----(2024-6-11)-(2024-6-17)
</p/>fixed tag matching to work
</p/>fixed input related errors when spaces, ', or " used
</p/>added verification in create_service() and create_user()
</p/>fixed crash when already existing service created
</p/>fixed service_matching failing to print 
</p/>added more print staments in .get_services() for clarity
</p/>fixed error when quotes used in service/user names
</p/>added saving across sessions by changing .save() to write to a single file instead creating a new one for each.    
v0.3----(2024-6-4)-(2024-6-10)
</p/>changed Service.save() and User.save() to write python files for object creation.
</p/>added menu loop to main
</p/>changed User to child of Service
</p/>added create_service()
</p/>added get_input_type()
</p/>added get_choice()
</p/>added offer_options()
</p/>added get_YesNo()
</p/>added create_user() - not functional
v0.2----(2024-5-31)-(2024-6-3)
</p/>added a tag system to get_service
</p/>added get_service function
</p/>added user class
</p/>added distance_from_user() function
</p/>added Windows, Apple, Safeway, and Costco service objects
</p/>added Bob and Alice user objects
</p/>
v0.1
</p/>added Service class __init__()
</p/>added Service class save()
</p/>fixed config bug in .replit file
