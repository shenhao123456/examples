#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 14:04
# @Author  : shenhao
# @File    : xlwt_test.py
import StringIO

import xlwt


def ExportContentByJiraVersion(request, site_name=None, jira_version=None):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response[
        'Content-Disposition'] = 'attachment;filename={0}-{1}.xls'.format(site_name, jira_version)
    wb = xlwt.Workbook(encoding='utf-8')
    sheet_prd = wb.add_sheet('PRD')

    style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour 0x19;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """

    style_body = xlwt.easyxf("""
            font:
                name Arial,
                bold off,
                height 0XA0;
            align:
                wrap on,
                vert center,
                horiz left;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                             )
    style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
    style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")

    fmts = [
        'M/D/YY',
        'D-MMM-YY',
        'D-MMM',
        'MMM-YY',
        'h:mm AM/PM',
        'h:mm:ss AM/PM',
        'h:mm',
        'h:mm:ss',
        'M/D/YY h:mm',
        'mm:ss',
        '[h]:mm:ss',
        'mm:ss.0',
    ]
    style_body.num_format_str = fmts[0]

    # 1st line
    sheet_prd.write(0, 0, '发布单', style_heading)
    sheet_prd.write(0, 1, '组件', style_heading)
    sheet_prd.write(0, 2, '环境', style_heading)

    row = 1
    contents = XXX.objects.filter()
    for content in contents:
        sheet_prd.write(row, 0, content.name, style_body)
        sheet_prd.write(row, 1, content.app_name.name, style_body)
        sheet_prd.write(row, 2, content.deploy_status, style_body)
        # 第一行加宽
        sheet_prd.col(0).width = 100 * 50
        sheet_prd.col(1).width = 200 * 50
        sheet_prd.col(2).width = 50 * 50
        row += 1

    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response





