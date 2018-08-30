import sys
import os
from lib import manager
import mysql.connector

def main():
    conn = mysql.connector.connect( \
        host = m.config['mysql']['host'], \
        port = m.config['mysql']['port'], \
        user = m.config['mysql']['user'], \
        password = m.config['mysql']['password'], \
        database = m.config['mysql']['database'])
    cur = conn.cursor(buffered=True)

    f = open('sql/' + m.args.options[0], encoding='utf-8')
    sql = f.read()

    for result in cur.execute(sql, multi=True):
        m.logger.info(result.statement)
        m.logger.info(result.fetchall())

    conn.commit()

if __name__ == '__main__':
    program_name = os.path.splitext(os.path.basename(__file__))[0]
    with manager.Manager(program_name) as m:
        try:
            main()
        except Exception as e:
            m.logger.exception(e)
            sys.exit(1)
