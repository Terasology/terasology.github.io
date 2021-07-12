import React, { useState } from "react";
import { Badge, Modal, ModalBody, ModalFooter } from "reactstrap";

const MentorModal = ({ name, desc, tags, customInfo, timeZone, country }) => {
  const [modal, setModal] = useState(false);
  const toggle = () => setModal(!modal);
  let githubURL = "https://github.com/" + `${customInfo[2] && customInfo[2].value.text}`;

  return (
    <div>
      <div className="mt-4 ">
        <button
          type="button"
          onClick={toggle}
          className="btn btn-lg btn-primary border border-0 p-2 font-weight-bold"
        >
          More about me
        </button>
      </div>
      <Modal isOpen={modal} toggle={toggle}>
        <h3 className="mt-3 ml-3">{name}</h3>
        <hr />
        <h4 className="mt-3 ml-3 mb-0">Introduction: </h4>
        <ModalBody>
          <div className="h3">{desc}</div>
          <div className="mt-3 Modal-custominfo ">
            <span className="ml-3 Modal-customFiled">
              Github: <a href={githubURL}>@{customInfo[2]  && customInfo[2].value.text}</a>
            </span>
            <br />
            <span className="ml-3 Modal-customFiled">Country: {country}</span>
            <br />
            <span className="ml-3 Modal-customFiled">
              Local Time: {timeZone}
            </span>
          </div>
          <h6 className="mt-4">Talk to this mentor about :</h6>
          <div className="d-flex overflow-auto ">
            {tags && tags.map((tag) => {
              return (
                <div className="md-tag m-2">
                  <Badge>{tag.name}</Badge>
                </div>
              );
            })}
          </div>
        </ModalBody>
        <ModalFooter>
          <button
            type="button"
            onClick={toggle}
            className=" btn-primary border border-0 font-weight-bold"
          >
            Close
          </button>
        </ModalFooter>
      </Modal>
    </div>
  );
};

export default MentorModal;
