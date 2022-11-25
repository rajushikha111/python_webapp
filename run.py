from loginapp import app, db

if __name__ == '__main__':
    db.create_all() # first we need to create table other wise HUGE ERROR. Wasted-24hr :
    app.debug=True
    app.run(host='0.0.0.0')
