import React from 'react'
import './Header.css'
import { useTelegram } from '../../hooks/useTelegram';

const Header = () => {
    const {user, dataBase} = useTelegram();

    return (
        <div className={"wrapper"}>
            <div className={'header'}>
                <div className={'name'}>
                    {user?.first_name + " " + user?.last_name}
                </div>
                <div className='email'>
                    There will be inno email<br/>
                    after authentification
                </div>
                <div className='lvl-gems'>
                    <div className='lvl'>{dataBase.users[0].level} lvl</div>
                    <div className='gems'>{dataBase.users[0].gems} gems</div>
                </div>
            </div>

        </div>
        
    );
};

export default Header;