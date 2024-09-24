/*
 * lakeFS API
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package io.lakefs.clients.api;

import io.lakefs.clients.api.ApiException;
import io.lakefs.clients.api.model.AbortPresignMultipartUpload;
import io.lakefs.clients.api.model.AuthenticationToken;
import io.lakefs.clients.api.model.CompletePresignMultipartUpload;
import io.lakefs.clients.api.model.Error;
import io.lakefs.clients.api.model.ExternalLoginInformation;
import io.lakefs.clients.api.model.ExternalPrincipal;
import io.lakefs.clients.api.model.ExternalPrincipalCreation;
import io.lakefs.clients.api.model.ExternalPrincipalList;
import io.lakefs.clients.api.model.ObjectStats;
import io.lakefs.clients.api.model.PresignMultipartUpload;
import io.lakefs.clients.api.model.PullRequest;
import io.lakefs.clients.api.model.PullRequestBasic;
import io.lakefs.clients.api.model.PullRequestCreation;
import io.lakefs.clients.api.model.PullRequestCreationResponse;
import io.lakefs.clients.api.model.PullRequestsList;
import io.lakefs.clients.api.model.StagingLocation;
import io.lakefs.clients.api.model.StsAuthRequest;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ExperimentalApi
 */
@Ignore
public class ExperimentalApiTest {

    private final ExperimentalApi api = new ExperimentalApi();

    
    /**
     * Abort a presign multipart upload
     *
     * Aborts a presign multipart upload.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void abortPresignMultipartUploadTest() throws ApiException {
        String repository = null;
        String branch = null;
        String uploadId = null;
        String path = null;
        AbortPresignMultipartUpload abortPresignMultipartUpload = null;
                api.abortPresignMultipartUpload(repository, branch, uploadId, path, abortPresignMultipartUpload);
        // TODO: test validations
    }
    
    /**
     * Complete a presign multipart upload request
     *
     * Completes a presign multipart upload by assembling the uploaded parts.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void completePresignMultipartUploadTest() throws ApiException {
        String repository = null;
        String branch = null;
        String uploadId = null;
        String path = null;
        CompletePresignMultipartUpload completePresignMultipartUpload = null;
                ObjectStats response = api.completePresignMultipartUpload(repository, branch, uploadId, path, completePresignMultipartUpload);
        // TODO: test validations
    }
    
    /**
     * Initiate a multipart upload
     *
     * Initiates a multipart upload and returns an upload ID with presigned URLs for each part (optional). Part numbers starts with 1. Each part except the last one has minimum size depends on the underlying blockstore implementation. For example working with S3 blockstore, minimum size is 5MB (excluding the last part). 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createPresignMultipartUploadTest() throws ApiException {
        String repository = null;
        String branch = null;
        String path = null;
        Integer parts = null;
                PresignMultipartUpload response = api.createPresignMultipartUpload(repository, branch, path, parts);
        // TODO: test validations
    }
    
    /**
     * create pull request
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createPullRequestTest() throws ApiException {
        String repository = null;
        PullRequestCreation pullRequestCreation = null;
                PullRequestCreationResponse response = api.createPullRequest(repository, pullRequestCreation);
        // TODO: test validations
    }
    
    /**
     * attach external principal to user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createUserExternalPrincipalTest() throws ApiException {
        String userId = null;
        String principalId = null;
        ExternalPrincipalCreation externalPrincipalCreation = null;
                api.createUserExternalPrincipal(userId, principalId, externalPrincipalCreation);
        // TODO: test validations
    }
    
    /**
     * delete external principal from user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteUserExternalPrincipalTest() throws ApiException {
        String userId = null;
        String principalId = null;
                api.deleteUserExternalPrincipal(userId, principalId);
        // TODO: test validations
    }
    
    /**
     * perform a login using an external authenticator
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void externalPrincipalLoginTest() throws ApiException {
        ExternalLoginInformation externalLoginInformation = null;
                AuthenticationToken response = api.externalPrincipalLogin(externalLoginInformation);
        // TODO: test validations
    }
    
    /**
     * describe external principal by id
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getExternalPrincipalTest() throws ApiException {
        String principalId = null;
                ExternalPrincipal response = api.getExternalPrincipal(principalId);
        // TODO: test validations
    }
    
    /**
     * get pull request
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getPullRequestTest() throws ApiException {
        String repository = null;
        String pullRequest = null;
                PullRequest response = api.getPullRequest(repository, pullRequest);
        // TODO: test validations
    }
    
    /**
     * hard reset branch
     *
     * Relocate branch to refer to ref.  Branch must not contain uncommitted data.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void hardResetBranchTest() throws ApiException {
        String repository = null;
        String branch = null;
        String ref = null;
        Boolean force = null;
                api.hardResetBranch(repository, branch, ref, force);
        // TODO: test validations
    }
    
    /**
     * list pull requests
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listPullRequestsTest() throws ApiException {
        String repository = null;
        String prefix = null;
        String after = null;
        Integer amount = null;
        String status = null;
                PullRequestsList response = api.listPullRequests(repository, prefix, after, amount, status);
        // TODO: test validations
    }
    
    /**
     * list user external policies attached to a user
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listUserExternalPrincipalsTest() throws ApiException {
        String userId = null;
        String prefix = null;
        String after = null;
        Integer amount = null;
                ExternalPrincipalList response = api.listUserExternalPrincipals(userId, prefix, after, amount);
        // TODO: test validations
    }
    
    /**
     * perform a login with STS
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void stsLoginTest() throws ApiException {
        StsAuthRequest stsAuthRequest = null;
                AuthenticationToken response = api.stsLogin(stsAuthRequest);
        // TODO: test validations
    }
    
    /**
     * update pull request
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updatePullRequestTest() throws ApiException {
        String repository = null;
        String pullRequest = null;
        PullRequestBasic pullRequestBasic = null;
                api.updatePullRequest(repository, pullRequest, pullRequestBasic);
        // TODO: test validations
    }
    
}
