% SEM Calculate standard error of the mean of a set of numbers
%
% Very robust - v can be an array; a matrix (in which case sem is taken as though
% each column is a condition); or a cell array of matrices.
%
% TFB
%
function s = sem(v)
  if numel(v) ~= length(v)
    % Do it by column:
    s = std(v) ./ sqrt(size(v,1));
  else
    if iscell(v)
      % Do each row separately:
      s = cellfun(@(vv)(std(vv)./sqrt(length(vv))), v);
    else
      % Treat as normal array:
      s = std(v) ./ sqrt(length(v));
    end
  end
end