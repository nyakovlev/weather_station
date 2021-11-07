import styled from "styled-components";
import { useState, useEffect } from "react";
import icon from "./anemometer.svg";

const AnemometerElement = styled.div`
    width: 100px;
    height: 100px;
    position: relative;
    img {
        position: absolute;
        width: 100%;
        height: 100%;
    }
`;

const stat = {
    value: null
};

function manageRotate(elem) {
    let rotation = 0;
    setInterval(() => {
        // console.log(stat.value);
        if (stat.value) {
            if (stat.value > 1270) {
                let ratio = (stat.value - 1270) / 700;
                let added = 1 + ratio * 50;
                rotation = rotation + added;
                elem.style.transform = `rotate(${rotation}deg)`;
            }
        }
    }, 50);
}

export default function Anemometer({ stats }) {
    useEffect(() => stats.subscribe(newStats => {
        let anem = newStats.find(newStat => newStat.name == "anemometer");
        stat.value = anem.value;
    }));

    return (
        <AnemometerElement ref={elem => manageRotate(elem)}>
            <img src={icon} />
        </AnemometerElement>
    );
}
