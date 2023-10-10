const tg = window.Telegram.WebApp;

export function useTelegram() {


    var dataBase = {
        // id is invalid since I do not want to be spammed
        users: [ {id: 100000000,
            level: 2,
            hours: 14,
            gems: 10,
            sxp: 20,
            challenges: [{id: 0, progress: 37, need: 50, isFinished: false}, {id: 1, progress: 19, need: 30, isFinished: false}, {id: 2, progress: 1, need: 1, isFinished: true}, {id: 3, progress: 5, need: 20, isFinished: false}]
        }
        ]
    }

    const onClose = () => {
        tg.close();
    }

    const onToggleButton  = () => {
        if(tg.MainButton.isVisible) {
            tg.MainButton.hide();
        } else {
            tg.MainButton.show();
        }
    }
    return {
        onClose,
        onToggleButton,
        tg,
        dataBase,
        user: tg.initDataUnsafe?.user
    }
}