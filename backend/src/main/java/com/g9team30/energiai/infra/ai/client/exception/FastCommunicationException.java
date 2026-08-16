package com.g9team30.energiai.infra.ai.client.exception;

public class FastCommunicationException extends RuntimeException {
    public FastCommunicationException(String message) {
        super(message);
    }

    public FastCommunicationException(String message, Throwable cause) {
        super(message, cause);
    }
}
