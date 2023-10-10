import React from "react"
import firstImage from "../../static/0.png"
import secondImage from "../../static/1.png"
import thirdImage from "../../static/2.png"
import fourthImage from "../../static/3.png"
import Button from "../../Button/Button";
import ProgressBar from "../../ProgressBar/ProgressBar"

const images = [
    firstImage,
    secondImage,
    thirdImage,
    fourthImage
]

const PartialChallenge = (data) => {
    console.log(data);

    const shortDescription = (description) => {
        return description.slice(0,50) + "...";
    }

    // const clickHandler = () => {

    // }
    return (
        <div className={"challenge"}>
            <div className={"challenge-left-module"}>
                <img src={images[data.content.challenge.info.id]} alt="Сhallenge reward" />
                <div className="rewards">
                    <div className={"points"}>{data.content.challenge.info.points} points</div>
                    <div className={"gems-ch"}>{data.content.challenge.info.gems} gems</div>
                </div>
            </div>
            <div className={"challenge-center-module"}>
                <ProgressBar
                    type = "Challenge Bar"
                    name = {data.content.challenge.info.title}
                    need = {data.content.challenge.info.need}
                    actual = {data.content.challenge.progress?.progress}
                    description = {shortDescription(data.content.challenge.info?.description)}
                />  
            </div>
            <div className="challenge-right-module">
                <Button onClick={data.clickHandler}>
                    Details
                </Button>
            </div>
        </div>
    )
};

export default PartialChallenge;
