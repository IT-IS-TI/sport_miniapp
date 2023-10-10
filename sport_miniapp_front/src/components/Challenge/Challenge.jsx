import React, { useState } from "react"
import './Challenge.css'
import PartialChallenge from "../Chellenges/PartialChellenge/PartialChallenge";

const Challenge = (item) => {
    
    const clickHandler = () => {
        if(item.type == "Partial") {
            console.log("Hi");
            setChallengeContent(
            <PartialChallenge
                content={item}
                onClickHandler={clickHandler}
            />);
        } else if (item.type == "Full") {
            setChallengeContent(
                <FullChallenge
                    content={item}
                    onClickHandler={clickHandler}
                />);
        } else if (item.type == "LB") {
            setChallengeContent(
                <LBChallenge
                    content={item}
                    onClickHandler={clickHandler}
                />);
        }
    }

    const [challengeContent, setChallengeContent] = useState(() => {
        if(item.type == "Partial") {
            console.log("Hi");
            return(
            <PartialChallenge
                content={item}
                onClickHandler={clickHandler}
            />);
        } else if (item.type == "Full") {
            return(
                <FullChallenge
                    content={item}
                    onClickHandler={clickHandler}
                />);
        } else if (item.type == "LB") {
            return(
                <LBChallenge
                    content={item}
                    onClickHandler={clickHandler}
                />);
        }
    });

    console.log(challengeContent);
    return (
        <div>
            {challengeContent}
        </div>
    );  
};

export default Challenge;
