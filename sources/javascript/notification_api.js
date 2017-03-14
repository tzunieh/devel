/* Browser Notification Resources
 * Spec: https://notifications.spec.whatwg.org/
 * MDN: https://developer.mozilla.org/en-US/docs/Web/API/Notification
 */

function notify(title, body, icon) {
    if ('Notification' in window) {
        var notification = {},
            msg_title = title || '',
            msg_body = {'body': body || '', 'icon': icon || ''};

        if (Notification.permission === 'granted') {
             notification = new Notification(msg_title, msg_body);

        } else if (Notification.permission !== 'denied') {
            Notification.requestPermission().then(function(permission) {
                if (permission === "granted") {
                    notification = new Notification(msg_title, msg_body);
                }
            });
        }
    }
}

notify(
    'Good Day!',
    'The is the message example. Please check the source code to see how to implement it.',
    'http://orig15.deviantart.net/a213/f/2014/191/e/e/lol_by_pikachumaster-d7q451j.gif'
)