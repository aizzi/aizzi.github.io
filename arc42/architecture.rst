..
   =============================================================================
   This template is provided as a guide to follow in writing architectural documentation for VAS modules and applications.
   
   Usage of the template is not enforced, but it is strongly recommended to provide uniformity and coherence across the whole platform.

   The repository is initialized for usage with Sphinx to generate documentation.
   =============================================================================

.. important::

   The *hint* sections are provided for guidance only. Remove them before publishing the final document.

============
Architecture
============

----------------------
Introduction and Goals
----------------------

.. hint::

   Describes the relevant requirements and the driving forces that software
   architects and development team must consider. These include

   -  underlying business goals, essential features and functional
      requirements for the system

   -  quality goals for the architecture

   -  relevant stakeholders and their expectations

Functional Requirements
=======================

.. hint::

   **Contents.**

   Short description of the functional requirements, driving forces,
   extract (or abstract) of requirements. Link to (hopefully existing)
   requirements documents (with version number and information where to
   find it).

   **Motivation.**

   From the point of view of the end users a system is created or modified
   to improve support of a business activity and/or improve the quality.

   **Form.**

   Short textual description, probably in tabular use-case format. If
   requirements documents exist this overview should refer to these
   documents.

   Keep these excerpts as short as possible. Balance readability of this
   document with potential redundancy w.r.t to requirements documents.

.. csv-table:: Functional Requirements
   :widths: auto
   :header-rows: 1
   :name: bdd_functional_requirements
   :file: tables/vas-app-bdd_fr.csv

Non-Functional Requirements
===========================

.. hint::

   **Contents.**

   The top three (max five) quality goals for the architecture whose
   fulfillment is of highest importance to the major stakeholders. We
   really mean quality goals for the architecture. Don’t confuse them with
   project goals. They are not necessarily identical.

   **Motivation.**

   You should know the quality goals of your most important stakeholders,
   since they will influence fundamental architectural decisions. Make sure
   to be very concrete about these qualities, avoid buzzwords. If you as an
   architect do not know how the quality of your work will be judged …

   **Form.**

   A table with quality goals and concrete scenarios, ordered by priorities

.. hint::

   Examples of Non-Functional Requirements as defined in `ISO25010 standard <https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-1:v1:en:sec:4.2>`_ are visible in the :ref:`nfr_map` below. Choose the ones that apply to your architecture.

   .. uml:: diagrams/type_of_nfr.puml
      :name: nfr_map
      :caption: Type of Non-Functional Requirements

.. csv-table:: Non-Functional Requirements
   :widths: auto
   :header-rows: 1
   :name: bdd_nfr
   :file: tables/vas-app-bdd_nfr.csv

Stakeholders
============

.. hint::

   **Contents.**

   Explicit overview of stakeholders of the system, i.e. all person, roles
   or organizations that

   -  should know the architecture

   -  have to be convinced of the architecture

   -  have to work with the architecture or with code

   -  need the documentation of the architecture for their work

   -  have to come up with decisions about the system or its development

   **Motivation.**

   You should know all parties involved in development of the system or
   affected by the system. Otherwise, you may get nasty surprises later in
   the development process. These stakeholders determine the extent and the
   level of detail of your work and its results.

   **Form.**

   Table with role names, person names, and their expectations with respect
   to the architecture and its documentation.

   +-------------+---------------------------+---------------------------+
   | Role/Name   | Contact                   | Expectations              |
   +=============+===========================+===========================+
   | *<Role-1>*  | *<Contact-1>*             | *<Expectation-1>*         |
   +-------------+---------------------------+---------------------------+
   | *<Role-2>*  | *<Contact-2>*             | *<Expectation-2>*         |
   +-------------+---------------------------+---------------------------+

.. csv-table:: Stakeholders
   :widths: auto
   :header-rows: 1
   :name: bdd_stk
   :file: tables/vas-app-bdd_stk.csv

----

------------------------
Architecture Constraints
------------------------

.. hint::

   **Contents.**

   Any requirement that constrains software architects in their freedom of
   design and implementation decisions or decision about the development
   process. These constraints sometimes go beyond individual systems and
   are valid for whole organizations and companies.

   **Motivation.**

   Architects should know exactly where they are free in their design
   decisions and where they must adhere to constraints. Constraints must
   always be dealt with; they may be negotiable, though.

   **Form.**

   Simple tables of constraints with explanations. If needed you can
   subdivide them into technical constraints, organizational and political
   constraints and conventions (e.g. programming or versioning guidelines,
   documentation or naming conventions)

Business Constraints
====================

.. hint::

   *Business Constraints (BCN)* are typically restrictions on budget, time and resources but can be any type of limitation related to business. Some example of BCN are:

   * *Schedule* - The delivery date for the product. The system must be ready for that date
   * *Budget* - The final system must cost less than a determined amount
   * *Team* - Composition of development team 
   * *Software Licensing* - Usage of a specific software is mandated

.. csv-table:: Business Constraints
   :widths: auto
   :header-rows: 1
   :name: bdd_bcn
   :file: tables/vas-app-bdd_bcn.csv

Technical Constraints
=====================

.. hint::

   *Technical Constraints (TCS)* are fixed decisions that canno be changed. They can be external or internal to the team. Some examples of TCN include:

   * Programming Language
   * Operating system or platforms supported
   * Use of a specific library or framework

.. csv-table:: Technical Constraints
   :widths: auto
   :header-rows: 1
   :name: bdd_tcn
   :file: tables/vas-app-bdd_tcn.csv

----

------------------------
System Scope and Context
------------------------

.. hint::

   **Contents.**

   This diagram shows the connection of the System with external entities, being those either Users or External Systems. All systems here are considered as black boxes, with the diagram showing the fows of information/control between them. The focus here is about how the System interacts with the external world, defined as whatever you do not have responsibility or control over.

   **Motivation.**

   The domain interfaces and technical interfaces to communication partners
   are among your system’s most critical aspects. Make sure that you
   completely understand them.

   **Form.**

   -  Context diagram.

.. uml:: diagrams/vas-app-bdd_sc.puml
   :name: system_context
   :caption: System Context

Actors
======

.. hint::

   **Contents.**

   Description of all the Actors (either humans or IT-systems) interacting with your System.
   Optionally you can add domain specific formats or communication protocols.

   **Motivation.**

   All stakeholders should understand which data are exchanged with the
   environment of the system.

   **Form.**

   +-------+-------------------+----------------+--------------------------------------------------+
   | ID    | Name              | Type           | Description                                      |
   +=======+===================+================+==================================================+
   | ACTxx | Name of the Actor | Human / System | Describe how the actor interacts with the system |
   +-------+-------------------+----------------+--------------------------------------------------+

.. csv-table:: Actors
   :widths: auto
   :header-rows: 1
   :name: bdd_act
   :file: tables/vas-app-bdd_act.csv


Control Flow
============

.. hint::

   **Contents.**

   Description of the control interfaces with the System.

   **Motivation.**

   Many stakeholders make architectural decision based on the technical
   interfaces between the system and its context. Especially infrastructure
   or hardware designers decide these technical interfaces.

   **Form.**

   +------+--------------------------+------+----+-------------------------------------------+
   | ID   | Control Flow             | From | To | Content                                   |
   +======+==========================+======+====+===========================================+
   | CFxx | Name of the Control Flow |      |    | Describe the Control using this interface |
   +------+--------------------------+------+----+-------------------------------------------+

.. csv-table:: Control Flows
   :widths: auto
   :header-rows: 1
   :name: bdd_cfl
   :file: tables/vas-app-bdd_cfl.csv

Information Flow
================

.. hint::

   **Contents.**

   Description of the data flowing between the System and the external interfaces.

   **Motivation.**

   Many stakeholders make architectural decision based on the technical
   interfaces between the system and its context. Especially infrastructure
   or hardware designers decide these technical interfaces.

   **Form.**

   +------+--------------------------+------+----+----------+-----------------------------------------------------+
   | ID   | Information Flow         | From | To | Bi-Di    | Content                                             |
   +======+==========================+======+====+==========+=====================================================+
   | IFxx | Name of the Control Flow |      |    | YES / NO | Describe the data flowing through this interface    |
   +------+--------------------------+------+----+----------+-----------------------------------------------------+

.. csv-table:: Information Flows
   :widths: auto
   :header-rows: 1
   :name: bdd_ifl
   :file: tables/vas-app-bdd_ifl.csv

----

-----------------
Solution Strategy
-----------------

.. hint::

   **Contents.**

   A short summary and explanation of the fundamental decisions and solution strategies, that shape the system’s architecture. These include

   -  technology decisions

   -  decisions about the top-level decomposition of the system, e.g. usage of an architectural pattern or design pattern

   -  decisions on how to achieve key quality goals

   -  relevant organizational decisions, e.g. selecting a development process or delegating certain tasks to third parties.

   **Motivation.**

   These decisions form the cornerstones for your architecture. They are the basis for many other detailed decisions or implementation rules.

   **Form.**

   Keep the explanation of these key decisions short.

   Motivate what you have decided and why you decided that way, based upon
   your problem statement, the quality goals and key constraints. Refer to
   details in the following sections.

----

-------------------
Building Block View
-------------------

.. hint::

   **Content.**

   The building block view shows the static decomposition of the system
   into building blocks (modules, components, subsystems, classes,
   interfaces, packages, libraries, frameworks, layers, partitions, tiers,
   functions, macros, operations, datas structures, …) as well as their
   dependencies (relationships, associations, …)

   This view is mandatory for every architecture documentation. In analogy
   to a house this is the *floor plan*.

   **Motivation.**

   Maintain an overview of your source code by making its structure
   understandable through abstraction.

   This allows you to communicate with your stakeholder on an abstract
   level without disclosing implementation details.

   **Form.**

   The building block view is a hierarchical collection of black boxes and
   white boxes and their descriptions, following the `C4 Model <https://c4model.com/>`_.

   **Containers** is the white box description of the overall system together
   with black box descriptions of all contained building blocks.

   **Components** zooms into some container. Thus it contains
   the white box description of selected building blocks of container,
   together with black box descriptions of their internal building blocks.

   **Code** zooms into selected building blocks of components.

Container diagram
=================

.. hint::

   In the C4 model, a container represents an application or a data store. A container is something that needs to be running in order for the overall software system to work.

   A container is essentially a context or boundary inside which some some is executed or some data is stored. And each container is a separately deployable/runnable thing or runtime environment, typically (but not always) running in its own process space. Because of this, communication between containers typically takes the form of an inter-process communication.

   **Form**

   A diagram with a table explaining the different components.

   +---------+---------------------+--------------+----------------------------+
   | ID      | Group               | Container    | Description                |
   +=========+=====================+==============+============================+
   | CNT01   | In case needed      |              |                            |
   +---------+---------------------+--------------+----------------------------+

.. uml:: diagrams/vas-app-bdd_cnt.puml
   :name: bdd_cnt_dgm
   :caption: BDD Container Diagram

.. csv-table:: BDD Containers
   :widths: auto
   :header-rows: 1
   :name: bdd_cnt_tbl
   :file: tables/vas-app-bdd_cnt.csv


Component Diagram
=================

.. hint::

   A component is a grouping of related functionality encapsulated behind a well-defined interface. 
   
   An important point to note is that all components inside a container typically execute in the same process space. **In the C4 model, components are not separately deployable units**.

   **Form**

   A series of diagrams with associated descriptions. 

.. uml:: diagrams/vas-app-bdd_cmp.puml
   :name: bdd_cmp_dgm
   :caption: BDD Component Diagram


Class diagram
=============

.. hint::

   This is an optional section. Ideally, you can generate it documenting your code and can be delivered in separate sections of the overall documentation.

----

------------
Runtime View
------------

.. hint::

   **Contents.**

   The runtime view describes concrete behavior and interactions of the
   system’s building blocks in form of scenarios from the following areas:

   -  important use cases or features: how do building blocks execute them?

   -  interactions at critical external interfaces: how do building blocks
      cooperate with users and neighboring systems?

   -  operation and administration: launch, start-up, stop

   -  error and exception scenarios

   Remark: The main criterion for the choice of possible scenarios
   (sequences, workflows) is their **architectural relevance**. It is
   **not** important to describe a large number of scenarios. You should
   rather document a representative selection.

   **Motivation.**

   You should understand how (instances of) building blocks of your system
   perform their job and communicate at runtime. You will mainly capture
   scenarios in your documentation to communicate your architecture to
   stakeholders that are less willing or able to read and understand the
   static models (building block view, deployment view).

   **Form.**

   There are many notations for describing scenarios, e.g.

   -  numbered list of steps (in natural language)

   -  activity diagrams or flow charts

   -  sequence diagrams

   -  BPMN or EPCs (event process chains)

   -  state machines

User's Authentication Request
=============================

.. uml:: diagrams/vas-app-bdd_uc01.puml
   :name: bdd_uc01_dgm
   :caption: User's Authentication

----

---------------
Deployment View
---------------

.. hint::

   **Content.**

   The deployment view describes:

   1. the technical infrastructure used to execute your system, with
      infrastructure elements like geographical locations, environments,
      computers, processors, channels and net topologies as well as other
      infrastructure elements and

   2. the mapping of (software) building blocks to that infrastructure
      elements.

   Often systems are executed in different environments, e.g. development
   environment, test environment, production environment. In such cases you
   should document all relevant environments.

   Especially document the deployment view when your software is executed
   as distributed system with more then one computer, processor, server or
   container or when you design and construct your own hardware processors
   and chips.

   From a software perspective it is sufficient to capture those elements
   of the infrastructure that are needed to show the deployment of your
   building blocks. Hardware architects can go beyond that and describe the
   infrastructure to any level of detail they need to capture.

   **Motivation.**

   Software does not run without hardware. This underlying infrastructure
   can and will influence your system and/or some cross-cutting concepts.
   Therefore, you need to know the infrastructure.

   Maybe the highest level deployment diagram is already contained in
   section 3.2. as technical context with your own infrastructure as ONE
   black box. In this section you will zoom into this black box using
   additional deployment diagrams:

   -  UML offers deployment diagrams to express that view. Use it, probably
      with nested diagrams, when your infrastructure is more complex.

   -  When your (hardware) stakeholders prefer other kinds of diagrams
      rather than the deployment diagram, let them use any kind that is
      able to show nodes and channels of the infrastructure.

----

----------------------
Cross-cutting Concepts
----------------------

.. hint::

   **Content.**

   This section describes overall, principal regulations and solution ideas
   that are relevant in multiple parts (= cross-cutting) of your system.
   Such concepts are often related to multiple building blocks. They can
   include many different topics, such as

   -  domain models

   -  architecture patterns or design patterns

   -  rules for using specific technology

   -  principal, often technical decisions of overall decisions

   -  implementation rules

   **Motivation.**

   Concepts form the basis for *conceptual integrity* (consistency,
   homogeneity) of the architecture. Thus, they are an important
   contribution to achieve inner qualities of your system.

   Some of these concepts cannot be assigned to individual building blocks
   (e.g. security or safety). This is the place in the template that we
   provided for a cohesive specification of such concepts.

   **Form.**

   The form can be varied:

   -  concept papers with any kind of structure

   -  cross-cutting model excerpts or scenarios using notations of the
      architecture views

   -  sample implementations, especially for technical concepts

   -  reference to typical usage of standard frameworks (e.g. using
      Hibernate for object/relational mapping)

   **Structure.**

   A potential (but not mandatory) structure for this section could be:

   -  Domain concepts

   -  User Experience concepts (UX)

   -  Safety and security concepts

   -  Architecture and design patterns

   -  "Under-the-hood"

   -  development concepts

   -  operational concepts

----

----------------
Design Decisions
----------------

.. hint::

   **Contents.**

   Important, expensive, large scale or risky architecture decisions
   including rationals. With "decisions" we mean selecting one alternative
   based on given criteria.

   Please use your judgement to decide whether an architectural decision
   should be documented here in this central section or whether you better
   document it locally (e.g. within the white box template of one building
   block).

   Avoid redundancy. Refer to section 4, where you already captured the
   most important decisions of your architecture.

   **Motivation.**

   Stakeholders of your system should be able to comprehend and retrace
   your decisions.

   **Form.**

   Various options:

   -  List or table, ordered by importance and consequences or:

   -  more detailed in form of separate sections per decision

   -  ADR (architecture decision record) for every important decision

----

.. _quality-scenarios:

-----------------
Quality Scenarios
-----------------

.. hint::

   **Content.**

   This section contains all quality requirements as quality tree with
   scenarios. The most important ones have already been described in
   section 1.2. (quality goals)

   Here you can also capture quality requirements with lesser priority,
   which will not create high risks when they are not fully achieved.

   **Motivation.**

   Since quality requirements will have a lot of influence on architectural
   decisions you should know for every stakeholder what is really important
   to them, concrete and measurable.

----

-------------------------
Risks and Technical Debts
-------------------------

.. hint::

   **Contents.**

   A list of identified technical risks or technical debts, ordered by
   priority

   **Motivation.**

   “Risk management is project management for grown-ups” (Tim Lister,
   Atlantic Systems Guild.)

   This should be your motto for systematic detection and evaluation of
   risks and technical debts in the architecture, which will be needed by
   management stakeholders (e.g. project managers, product owners) as part
   of the overall risk analysis and measurement planning.

   **Form.**

   List of risks and/or technical debts, probably including suggested
   measures to minimize, mitigate or avoid risks or reduce technical debts.

----

--------
Glossary
--------

.. hint::

   **Contents.**

   The most important domain and technical terms that your stakeholders use
   when discussing the system.

   You can also see the glossary as source for translations if you work in
   multi-language teams.

   **Motivation.**

   You should clearly define your terms, so that all stakeholders

   -  have an identical understanding of these terms

   -  do not use synonyms and homonyms

   **Form.**

   A table with columns <Term> and <Definition>.

   Potentially more columns in case you need translations.

   +-----------------------------------+-----------------------------------+
   | Term                              | Definition                        |
   +===================================+===================================+
   | <Term-1>                          | <definition-1>                    |
   +-----------------------------------+-----------------------------------+
   | <Term-2>                          | <definition-2>                    |
   +-----------------------------------+-----------------------------------+

----

-------------------
About this template
-------------------

+---------+--------------------------------------------------------------------+
| |arc42| |  This template is derived from arch42, the Template for            |
|         |  documentation of software and system architecture, with the       |
|         |  following changes to accomodate the                               |
|         |  `C4 Architectural Language <https://c4model.com/>`_:              |
|         |                                                                    |
|         |  * Context and Scope ==> System Context Diagram                    |
|         |  * Building Block View (level 1) ==> Container Diagram             |
|         |  * Building Block View (level 2) ==> Component Diagram             |
|         |  * Building Block View (level 3) ==> Class Diagram                 |
|         |                                                                    |
|         |  By Dr. Gernot Starke, Dr. Peter Hruschka and contributors.        |
|         |                                                                    |
|         |  Template Revision: 7.0 EN (based on asciidoc), January 2017       |
|         |                                                                    |
|         |  © We acknowledge that this document uses material from the arc 42 |
|         |  architecture template, https://arc42.org/. Created by Dr. Peter   |
|         |  Hruschka & Dr. Gernot Starke.                                     |
+---------+--------------------------------------------------------------------+

.. |arc42| image:: images/arc42-logo.png