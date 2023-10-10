import React, { useState } from "react"
import './ChallengeList.css'
import Challenge from "../Challenge/Challenge";
import { useTelegram } from "../../hooks/useTelegram";
import Button from "../Button/Button";



const challenges = [
    {id: 0, title:"Top Sportsmen S23", description: "To complete the challenge Top Sportsmen you need to get 50 sport hours during the Spring23 semester. Top 10 students from this challenge will get additional reward - 10 xp and 2 gem. Note: In case if several people has the same amount of hour, the one who got them faster will be in the higher position.", points: 40, gems:10, need: 50},
    {id: 1, title:"Top Sportsmen Sum23", description: "To complete the challenge Top Sportsmen you need to get 30 sport hours during the Summer23 semester. Top 10 students from this challenge will get additional reward - 10 xp and 1 gem. Note: In case if several people has the same amount of hour, the one who got them faster will be in the higher position.", points: 20, gems: 5, need: 30},
    {id: 2, title:"Table Tennis Competition", description: "To complete the Table Tennis Competition challenge you need to participate in the event at 10th of May.", points: 20, gems: 0, need:1},
    {id: 3, title:"Football lover", description: "To complete the Football lover challenge you need to participate in 20 Football training sessions during Fall 2023 semester.", points: 15, gems: 0, need: 20},
]

const ChallengeList = () => {

    let inProcess = [];
    let finished = [];

    const {user, dataBase} = useTelegram();
    
    const client = dataBase.users.find((e) => {
        return e.id == 894797521;
    });


    client.challenges.forEach(e => {
        if(e.isFinished) {
            finished.push({
                info: challenges[e.id],
                progress: e
            });
        } else {
            inProcess.push({
                info: challenges[e.id],
                progress: e
            });
        }
    })
    let challengesStatus = "inProcess";

    const [listContent, setListContent] = useState(inProcess.map(item => (
        <Challenge
            challenge={item}
            className={'item'}
            type="Partial"
        />
    )));

    const showMyChallenges = () => {
        setListContent(finished.map(item => (
            <Challenge
                challenge={item}
                className={'item'}
                type="Partial"
            />
        )))
    }

    const showAllChallenges = () => {
        setListContent(inProcess.map(item => (
            <Challenge
                challenge={item}
                className={'item'}
                type="Partial"
            />
        )));  
    }
    
    return (
        <div className="container">
            <div className="challenge-list-head">
                <div className="title">Challenges</div>
                <div className="buttons-container">
                    <Button onClick={showAllChallenges}>All Challenges</Button>
                    <Button onClick={showMyChallenges}>My Challenges</Button>
                </div>
            </div>
            <div className={"list"}>{listContent}</div>
        </div>
    )
};

export default ChallengeList;
