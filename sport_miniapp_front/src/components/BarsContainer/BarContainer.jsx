import React from "react"
import './BarContainer.css'
import ProgressBar from "../ProgressBar/ProgressBar";

const BarContainer = () => {

    return (
        <div data-testid="list-of-two-progress-bars" className={"list"}>
            <ProgressBar
                type = "Sport hours"
                name = "Sport hours"
                needHours = "30"
                hours = "12"
                description = ""
            />
            <br/>
            <br/>  
            <ProgressBar
                type = "Sport points"
                name = "Sport points"
                needPoints = "1000"
                points = "120"
                description = ""
            />   
        </div>
  )
};

export default BarContainer;
