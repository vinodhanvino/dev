from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient, SignUpOptions
)

def send_otp():
    try:
        descope_client = DescopeClient(project_id='P2rypsFDrnnRusLgqp50SWeLAIJn')

        descope_client.otp.sign_up_or_in(
            method=DeliveryMethod.SMS,
            login_id="+919019687131"

        )

    except Exception as error:
        print("failed to initialize. Error:")
        print(error)

def verify_otp(code):
    try:
        descope_client = DescopeClient(project_id='P2rypsFDrnnRusLgqp50SWeLAIJn')
        jwt_response = descope_client.otp.verify_code(
            method=DeliveryMethod.SMS,
            login_id="+919019687131",
            code=code
        )
        session_token = jwt_response[SESSION_TOKEN_NAME].get("jwt")
        refresh_token = jwt_response[REFRESH_SESSION_TOKEN_NAME].get("jwt")
        print("session_token : ", session_token)
        print("refresh_token : ", refresh_token)
    except Exception as error:
        print("failed to initialize. Error:")
        print(error)

# send_otp()
verify_otp('950979')