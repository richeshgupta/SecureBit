import React, { useEffect, useContext } from "react";
import openSocket from "socket.io-client";
import { activeChatAction } from "./stateManagement/actions";
import { store } from "./stateManagement/store";

// const SOCKET_URL = "http://api.securebit.tech:2086/";
const SOCKET_URL = "http://localhost:9000/";
let socket;

const SocketService = () => {
  const {
    state: { userDetail },
    dispatch,
  } = useContext(store);

  const setupSocket = () => {
    socket = openSocket(SOCKET_URL);

    socket.on("command", (data) => {
      console.log("data",data);

      if (!userDetail) return;

      if (userDetail.id !== data.receiver) return;
      
      dispatch({ type: activeChatAction, payload: true });
    });
  };

  useEffect(setupSocket, [userDetail]);

  return <></>;
};

export default SocketService;

const sendSocket = (data) => {
  socket.emit("command", {
    type: data.type,
    id: data.id,
    content: data.content,
  });
};

export const sendTestSocket = (data) => {
  socket.emit("command", data);
  console.log("Data : ",data);
};
