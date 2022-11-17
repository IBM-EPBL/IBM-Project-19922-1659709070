import ibm_db

connection = ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=lmm13296;PWD=iuazyaTKenH6bpQk",'','')

print(connection)
print("Connection Successfull !\n\n")

# sql = "SELECT EMAIL,PASSWORD FROM logins"
# stmt = ibm_db.exec_immediate(connection, sql)
# dictionary = ibm_db.fetch_assoc(stmt)
# while dictionary != False:
#     # printing
#     print("Full Row : ", dictionary)
#     dictionary = ibm_db.fetch_assoc(stmt)