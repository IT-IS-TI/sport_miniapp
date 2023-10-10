import { useEffect } from "react";
import React from "react"
import './App.css';
import { useTelegram } from "./hooks/useTelegram";
import Header from "./components/Header/Header";
import ChallengeList from "./components/ChallengesList/ChallengeList";
import BarContainer from "./components/BarsContainer/BarContainer";

function App() {

  const {tg} = useTelegram();

  useEffect( () => {
    tg.ready();
  }, [])

  return (
    <div className="App">
      <Header />
      <BarContainer />
      <ChallengeList />
    </div>
  );
}

export default App;
