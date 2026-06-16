# Reusable Codex-Style Skills

These are sanitized personal examples of reusable AI workflow patterns. They are not employer skill files.

## 1. Requirements to Delivery Pack

**Purpose:** Convert a messy stakeholder request into structured SDLC artifacts.

**Inputs**
- Business request
- User roles
- Known constraints
- Existing process notes

**Outputs**
- Structured requirements JSON
- User stories
- Acceptance criteria
- UAT test cases
- Delivery handoff notes
- Open questions

**Review rules**
- Do not treat generated artifacts as approved.
- Flag assumptions.
- Require human review for requirements affecting finance, billing, compliance, or customer communication.

## 2. Snowflake Data Mapping Assistant

**Purpose:** Map a reporting request to a certified data catalog and produce a reviewable SQL draft.

**Inputs**
- Reporting request
- Data catalog
- Business field list
- Known source-of-truth rules

**Outputs**
- Field-to-source mapping
- Certified source flags
- SQL draft
- Validation rules
- Open questions

**Review rules**
- Flag non-certified sources.
- Check grain before joins.
- Validate row counts, null handling, and reconciliation logic.

## 3. UAT Test Generator

**Purpose:** Convert user stories and acceptance criteria into UAT scenarios.

**Outputs**
- Happy-path cases
- Negative cases
- Role-based cases
- Data-quality cases
- Release-blocking flags

## 4. API Payload Reviewer

**Purpose:** Review API payloads for missing fields, type mismatches, naming issues, and edge cases.

**Outputs**
- Issues found
- Corrected sample payload
- Validation rules
- Open questions

## 5. Workflow Risk Reviewer

**Purpose:** Review an automation workflow for operational risk before rollout.

**Outputs**
- Failure modes
- Human review points
- Monitoring needs
- Exception handling
- Rollback or manual fallback path
