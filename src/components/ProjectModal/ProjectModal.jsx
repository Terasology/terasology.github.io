import React, { useState } from "react";
import { Badge, Modal, ModalFooter } from "reactstrap";
import { Remarkable } from "remarkable";
import parse from "html-react-parser";

const ProjectModal = ({ name, desc, tags }) => {
  const [modal, setModal] = useState(false);
  const toggle = () => setModal(!modal);
  const md = new Remarkable();

  const descs = md.render(desc);

  return (
    <div>
      <div className="mt-4 ">
        <button
          type="button"
          onClick={toggle}
          className="btn btn-lg btn-primary border border-0 p-2 font-weight-bold"
        >
          Project Details
        </button>
      </div>

      <Modal className="modal-dialog modal-xl" isOpen={modal} toggle={toggle}>
        <h4 className="mt-3 ml-3">{name}</h4>
        <hr />
        <div className="m-4">
          <div className="m-3 overflow-auto">{parse(descs)}</div>
          <h6 className="mt-4 ml-2">Project Tags:</h6>
          <div className="d-flex overflow-auto ml-2 ">
            {tags &&
              tags.map((tag) => {
                return (
                  <div className="md-tag m-2">
                    <Badge>{tag.name}</Badge>
                  </div>
                );
              })}
          </div>
        </div>
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

export default ProjectModal;
