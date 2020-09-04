% SEMWITHIN Calculate within-subject standard error of a set of numbers by
% grand mean normalizing each subject's across-condition data to be the same.
%
% Very robust - v can be an array; a matrix (in which case sem is taken as though
% each column is a condition); or a cell array of matrices.
%
% TFB
%
function s = semWithin(v)
  if iscell(v)
    v = cellfun(@reshapeCells, v, 'UniformOutput', false);
    v = cell2mat(v);
  end
  if numel(v) ~= length(v)
    % Do it by column:
    subjectMeans = repmat(mean(v,2), [1, size(v,2)]);
    s = std(v-subjectMeans) ./ sqrt(size(v,1));
  else
    % Treat as normal array:
    s = std(v) ./ sqrt(length(v));
    warning('Only one condition was sent to semWithin, so giving back a normal SEM');
  end
end

% Reshape cells
function cc = reshapeCells(cc)
  if size(cc,2)>size(cc,1)
    cc=cc';
  end
end