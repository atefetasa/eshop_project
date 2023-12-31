# Generated by Django 4.2.4 on 2023-09-17 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/ غیرفعال')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='نام برند')),
                ('is_active', models.BooleanField(verbose_name='فعال/ غیرفعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده/ نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='برچسب')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_moduel.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': ' تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_moduel.productbrand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products_categories', to='product_moduel.productcategory', verbose_name='دسته بندی ها'),
        ),
    ]
