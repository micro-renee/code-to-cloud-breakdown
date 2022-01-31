from flask import Flask, request, render_template

invite_app = Flask('app')

@invite_app.route('/view', methods=('GET', 'POST'))
def view_invite():
  # date = "Wedensday 21st Marchtember"
  # time = "3:65pm:"
  # event = "Bibi's birthday party"
  # to = "Jack"
  # sender = "Renee"

  date = request.args.get('date')
  time = request.args.get('time')
  event = request.args.get('event')
  to = request.args.get('to')
  sender = request.args.get('sender')
  return render_template('invite-demo.html', event=event, invitee=to, date=date, time=time, sender=sender)

# http://192.168.1.122:8080/view?event=Bibi's+Bday&to=Johny&date=Monday+1st+of+Octember&time=4pm&sender=Bob




if __name__ == '__main__':
    invite_app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8080)