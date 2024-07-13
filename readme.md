# Profile Management System

Welcome to the Profile Management System! This simple Flask application is designed to demonstrate several common web vulnerabilities related to user session and authentication management. As you interact with the application, you will encounter scenarios that mimic real-world vulnerabilities in a safe and controlled environment. This will help you understand the risks associated with improper handling of user credentials and session data.

## Instructions
An example file has been created for you, `xsrf_POST.html`. This file demonstrates an attempt at a Cross-Site Request Forgery (XSRF) attack. To see the attack in action, drag the file icon into the browser icon. Ensure you are logged in to the Profile Management System before attempting the attack, and that you are not 'serving' the file from a web server, you want to open the file directly in the browser using the file:// protocol.

You will see the attack does NOT work. This leads us to your first task: 

1. Identify the settings/configurations in the  Profile Management System that prevents the CSRF attack from working. Explain how these settings/configurations prevent the attack.

### Here are the following tasks you need to complete:

2. Identify the settings/configurations in the Profile Management System that allows the Cross-Site Scripting (XSS) attack from working. Explain how these settings/configurations allow the attack. Supply two examples of XSS attacks that work against the Profile Management System.

3. Although the XSRF attack did not work, the Profile Management System is still vulnerable to XSRF attacks. Identify the settings/configurations in the Profile Management System that make it vulnerable to XSRF attacks. Explain how these settings/configurations allow the attack. Supply an example of an XSRF attack that works against the Profile Management System.

4. There is an additional attack vector for the cross-site scripting attack that is not covered in the previous task. Identify this attack vector and explain how it works. Hint: how can we trick the site into thinking our request is from the same origin?

5. Explain how to fix #2

6. Explain how to fix #3

7. Explain how to fix #4, you do not need to provide code, just a brief high-level explanation of the solution.


## Submission
Submit your answers in a PDF. Your submission should be a maximum of 3 pages, single-spaced, 12-point font. You should include the names of all the members of your group and the date on the submission. Your submission should be clear, concise, and well-organized. Your answers should be detailed and demonstrate a strong understanding of the concepts discussed in the Profile Management System.


## Resources
- [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf)
- [Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss)
- [PortSwigger SameSite Cookies](https://portswigger.net/web-security/csrf/samesite-cookies)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Flask Session Configuration](https://flask.palletsprojects.com/en/2.0.x/config/)

