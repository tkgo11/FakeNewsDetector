/* eslint-disable @typescript-eslint/no-this-alias */
/* eslint-disable no-undef */
const HIGHLIGHTER_ID = 'news-selector-highlighter';
let lastHighlightTarget;

function terminate() {
	// The `click` listener is automatically removed after it has been called once
	window.removeEventListener('mousemove', throttle(updateHighlight));
	window.removeEventListener('keydown', checkTerminateKeys);
	removeHighlight();
};

function addHighlight() {
	const div = document.createElement('div');
	div.id = HIGHLIGHTER_ID;
	const { style } = div;
	style.backgroundColor = '#1d234280';
	style.boxSizing = 'border-box';
	style.border = 'solid 4px #f0bb8980';
	style.position = 'fixed';
	style.zIndex = '9999';
	style.pointerEvents = 'none';
	document.body.appendChild(div);
};

function updateHighlight({ target }) {
	if (!(target instanceof HTMLElement) || target === lastHighlightTarget) {
		return;
	}
	lastHighlightTarget = target;
	const { top, left, width, height } = target.getBoundingClientRect();
	const highlighter = document.getElementById(HIGHLIGHTER_ID);
	if (!highlighter) return;
	const { style } = highlighter;
	style.top = top - 4 + 'px';
	style.left = left - 4 + 'px';
	style.width = width + 8 + 'px';
	style.height = height + 8 + 'px';
};

function removeHighlight() {
	const highlighter = document.getElementById(HIGHLIGHTER_ID);
	if (highlighter) {
		document.body.removeChild(highlighter);
	}
};

async function grabSelector(event) {
	removeHighlight();
    event.preventDefault();
    const { target } = event;
    if (!(target instanceof HTMLElement)) {
        terminate();
        return;
    }

    try {
        // Extract the text content from the target element
        const textValue = target.textContent.trim();

        const response = await fetch('http://localhost:5050/generate_selector', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // Send the text value instead of the selector
            body: JSON.stringify({ text: textValue })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.text();
        alert(result)
    } catch (err) {
        console.error('Error: ' + err)
    }
    terminate();
};

function generateSelector(element) {
	if (!element) return '';

	let selector = getSelector(element);
	while(!isUnique(selector) && element) {
		element = element.parentElement;
		const newSelector = getSelector(element);
		if(newSelector) selector = newSelector + '>' + selector;
	}

	return selector;
};

function getSelector(element) {
	if (!element) return '';

	// Use tag name, id, and class names to construct a selector
	let selector = element.tagName.toLowerCase();
	if (element.id) {
		selector += `#${element.id}`;
	} else if (element.className) {
		selector += `.${element.className.trim().replace(/\s+/g, '.')}`;
	}

	return selector;
};

function appendPseudoSelector(element, selector) {
	return isUnique(selector) ? selector : `${selector}:nth-child(${getChildIndex(element)})`;
};

function getChildIndex({ previousElementSibling: sibling }) {
	return sibling ? getChildIndex(sibling) + 1 : 1;
};

function getQueryLength(selector) {
	return document.querySelectorAll(selector).length;
};

function isUnique(selector) {
	return getQueryLength(selector) <= 1;
};

function checkTerminateKeys(event) {
	const { key } = event;
	if (key === 'Escape' || key === 'Esc') {
		event.preventDefault();
		terminate();
	}
};

function throttle(func, limit = 100) {
	let inThrottle;
	let lastResult;

	return function () {
		const args = arguments;
		const context = this

		if (!inThrottle) {
			inThrottle = true;
			setTimeout(() => (inThrottle = false), limit);
			lastResult = func.apply(context, args);
		}

		return lastResult;
	};
};
