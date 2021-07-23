# 9-11 导入Admin
import models

admin = models.Admin("Tom", "Young", "swim")

admin.privileges.show_privileges()
