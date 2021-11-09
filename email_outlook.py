import win32com.client

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.To = 'tester@hotmail.com'
mail.Subject = 'Sample Email'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "This is the normal body"
mail.Attachments.Add(r'C:\Users\thoma\OneDrive\Dokumenter\100daysofcode\e-mailsender_git\test.txt')
#mail.Attachments.Add('c:\\sample2.xlsx')
#mail.CC = 'somebody@company.com'

mail.Send()