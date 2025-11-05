# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from unittest import result
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11lll111l_opy_, bstack1l1l1lllll_opy_, bstack11lll111ll_opy_,
                                    bstack11l11llll1l_opy_, bstack11l1l11111l_opy_, bstack11l11ll111l_opy_, bstack11l1l11l1ll_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1llll1111l_opy_, bstack1l1lll11ll_opy_
from bstack_utils.proxy import bstack11l111l11_opy_, bstack1l111ll1ll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11111l1ll1_opy_
from bstack_utils.bstack1l1lll1lll_opy_ import bstack11l1l1l1l1_opy_
from browserstack_sdk._version import __version__
bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
logger = bstack11111l1ll1_opy_.get_logger(__name__, bstack11111l1ll1_opy_.bstack1l1l1ll111l_opy_())
def bstack111l11l1l11_opy_(config):
    return config[bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᰜ")]
def bstack111l111lll1_opy_(config):
    return config[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᰝ")]
def bstack1ll11ll111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111lll1ll1_opy_(obj):
    values = []
    bstack111l11l1lll_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡴࠥࡢࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࡞ࡧ࠯ࠩࠨᰞ"), re.I)
    for key in obj.keys():
        if bstack111l11l1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111lll11l1_opy_(config):
    tags = []
    tags.extend(bstack1111lll1ll1_opy_(os.environ))
    tags.extend(bstack1111lll1ll1_opy_(config))
    return tags
def bstack111l11l11l1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1111lll_opy_(bstack111l11l111l_opy_):
    if not bstack111l11l111l_opy_:
        return bstack11ll1ll_opy_ (u"ࠪࠫᰟ")
    return bstack11ll1ll_opy_ (u"ࠦࢀࢃࠠࠩࡽࢀ࠭ࠧᰠ").format(bstack111l11l111l_opy_.name, bstack111l11l111l_opy_.email)
def bstack111l1ll1111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1111l1l_opy_ = repo.common_dir
        info = {
            bstack11ll1ll_opy_ (u"ࠧࡹࡨࡢࠤᰡ"): repo.head.commit.hexsha,
            bstack11ll1ll_opy_ (u"ࠨࡳࡩࡱࡵࡸࡤࡹࡨࡢࠤᰢ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll1ll_opy_ (u"ࠢࡣࡴࡤࡲࡨ࡮ࠢᰣ"): repo.active_branch.name,
            bstack11ll1ll_opy_ (u"ࠣࡶࡤ࡫ࠧᰤ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࠧᰥ"): bstack111l1111lll_opy_(repo.head.commit.committer),
            bstack11ll1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࡥࡤࡢࡶࡨࠦᰦ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll1ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࠦᰧ"): bstack111l1111lll_opy_(repo.head.commit.author),
            bstack11ll1ll_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡤࡪࡡࡵࡧࠥᰨ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll1ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᰩ"): repo.head.commit.message,
            bstack11ll1ll_opy_ (u"ࠢࡳࡱࡲࡸࠧᰪ"): repo.git.rev_parse(bstack11ll1ll_opy_ (u"ࠣ࠯࠰ࡷ࡭ࡵࡷ࠮ࡶࡲࡴࡱ࡫ࡶࡦ࡮ࠥᰫ")),
            bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳ࡯࡯ࡡࡪ࡭ࡹࡥࡤࡪࡴࠥᰬ"): bstack111l1111l1l_opy_,
            bstack11ll1ll_opy_ (u"ࠥࡻࡴࡸ࡫ࡵࡴࡨࡩࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᰭ"): subprocess.check_output([bstack11ll1ll_opy_ (u"ࠦ࡬࡯ࡴࠣᰮ"), bstack11ll1ll_opy_ (u"ࠧࡸࡥࡷ࠯ࡳࡥࡷࡹࡥࠣᰯ"), bstack11ll1ll_opy_ (u"ࠨ࠭࠮ࡩ࡬ࡸ࠲ࡩ࡯࡮࡯ࡲࡲ࠲ࡪࡩࡳࠤᰰ")]).strip().decode(
                bstack11ll1ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᰱ")),
            bstack11ll1ll_opy_ (u"ࠣ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᰲ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡵࡢࡷ࡮ࡴࡣࡦࡡ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦᰳ"): repo.git.rev_list(
                bstack11ll1ll_opy_ (u"ࠥࡿࢂ࠴࠮ࡼࡿࠥᰴ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111l1111l1_opy_ = []
        for remote in remotes:
            bstack1111l11l1ll_opy_ = {
                bstack11ll1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᰵ"): remote.name,
                bstack11ll1ll_opy_ (u"ࠧࡻࡲ࡭ࠤᰶ"): remote.url,
            }
            bstack1111l1111l1_opy_.append(bstack1111l11l1ll_opy_)
        bstack1111ll1llll_opy_ = {
            bstack11ll1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᰷ࠦ"): bstack11ll1ll_opy_ (u"ࠢࡨ࡫ࡷࠦ᰸"),
            **info,
            bstack11ll1ll_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡴࠤ᰹"): bstack1111l1111l1_opy_
        }
        bstack1111ll1llll_opy_ = bstack1111lllll1l_opy_(bstack1111ll1llll_opy_)
        return bstack1111ll1llll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧ᰺").format(err))
        return {}
def bstack11ll1l1ll11_opy_(bstack1111l1l111l_opy_=None):
    bstack11ll1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࡢ࡮࡯ࡽࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡺࡹࡥࠡࡥࡤࡷࡪࡹࠠࡧࡱࡵࠤࡪࡧࡣࡩࠢࡩࡳࡱࡪࡥࡳࠢ࡬ࡲࠥࡺࡨࡦࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡬࡯࡭ࡦࡨࡶࡸࠦࠨ࡭࡫ࡶࡸ࠱ࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪ࠼ࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡓࡵ࡮ࡦ࠼ࠣࡑࡴࡴ࡯࠮ࡴࡨࡴࡴࠦࡡࡱࡲࡵࡳࡦࡩࡨ࠭ࠢࡸࡷࡪࡹࠠࡤࡷࡵࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡠࡵࡳ࠯ࡩࡨࡸࡨࡽࡤࠩࠫࡠࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡊࡳࡰࡵࡻࠣࡰ࡮ࡹࡴࠡ࡝ࡠ࠾ࠥࡓࡵ࡭ࡶ࡬࠱ࡷ࡫ࡰࡰࠢࡤࡴࡵࡸ࡯ࡢࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡱࡳࠥࡹ࡯ࡶࡴࡦࡩࡸࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦ࠯ࠤࡷ࡫ࡴࡶࡴࡱࡷࠥࡡ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡎ࡬ࡷࡹࠦ࡯ࡧࠢࡳࡥࡹ࡮ࡳ࠻ࠢࡐࡹࡱࡺࡩ࠮ࡴࡨࡴࡴࠦࡡࡱࡲࡵࡳࡦࡩࡨࠡࡹ࡬ࡸ࡭ࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࠡࡨࡲࡰࡩ࡫ࡲࡴࠢࡷࡳࠥࡧ࡮ࡢ࡮ࡼࡾࡪࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡤࡪࡥࡷࡷ࠱ࠦࡥࡢࡥ࡫ࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡦࠦࡦࡰ࡮ࡧࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᰻")
    if bstack1111l1l111l_opy_ is None:
        bstack1111l1l111l_opy_ = [os.getcwd()]
    elif isinstance(bstack1111l1l111l_opy_, list) and len(bstack1111l1l111l_opy_) == 0:
        return []
    results = []
    for folder in bstack1111l1l111l_opy_:
        try:
            if not os.path.exists(folder):
                raise Exception(bstack11ll1ll_opy_ (u"ࠦࡋࡵ࡬ࡥࡧࡵࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤ᰼").format(folder))
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11ll1ll_opy_ (u"ࠧࡶࡲࡊࡦࠥ᰽"): bstack11ll1ll_opy_ (u"ࠨࠢ᰾"),
                bstack11ll1ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᰿"): [],
                bstack11ll1ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤ᱀"): [],
                bstack11ll1ll_opy_ (u"ࠤࡳࡶࡉࡧࡴࡦࠤ᱁"): bstack11ll1ll_opy_ (u"ࠥࠦ᱂"),
                bstack11ll1ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡑࡪࡹࡳࡢࡩࡨࡷࠧ᱃"): [],
                bstack11ll1ll_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨ᱄"): bstack11ll1ll_opy_ (u"ࠨࠢ᱅"),
                bstack11ll1ll_opy_ (u"ࠢࡱࡴࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠢ᱆"): bstack11ll1ll_opy_ (u"ࠣࠤ᱇"),
                bstack11ll1ll_opy_ (u"ࠤࡳࡶࡗࡧࡷࡅ࡫ࡩࡪࠧ᱈"): bstack11ll1ll_opy_ (u"ࠥࠦ᱉")
            }
            bstack111l1l1lll1_opy_ = repo.active_branch.name
            bstack1111l1ll111_opy_ = repo.head.commit
            result[bstack11ll1ll_opy_ (u"ࠦࡵࡸࡉࡥࠤ᱊")] = bstack1111l1ll111_opy_.hexsha
            bstack1111l1l11ll_opy_ = _1111ll1l111_opy_(repo)
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡈࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡪࡴࡸࠠࡤࡱࡰࡴࡦࡸࡩࡴࡱࡱ࠾ࠥࠨ᱋") + str(bstack1111l1l11ll_opy_) + bstack11ll1ll_opy_ (u"ࠨࠢ᱌"))
            if bstack1111l1l11ll_opy_:
                try:
                    bstack111l111ll1l_opy_ = repo.git.diff(bstack11ll1ll_opy_ (u"ࠢ࠮࠯ࡱࡥࡲ࡫࠭ࡰࡰ࡯ࡽࠧᱍ"), bstack1lll1ll1l11_opy_ (u"ࠣࡽࡥࡥࡸ࡫࡟ࡣࡴࡤࡲࡨ࡮ࡽ࠯࠰࠱ࡿࡨࡻࡲࡳࡧࡱࡸࡤࡨࡲࡢࡰࡦ࡬ࢂࠨᱎ")).split(bstack11ll1ll_opy_ (u"ࠩ࡟ࡲࠬᱏ"))
                    logger.debug(bstack11ll1ll_opy_ (u"ࠥࡇ࡭ࡧ࡮ࡨࡧࡧࠤ࡫࡯࡬ࡦࡵࠣࡦࡪࡺࡷࡦࡧࡱࠤࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀࠤࡦࡴࡤࠡࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀ࠾ࠥࠨ᱐") + str(bstack111l111ll1l_opy_) + bstack11ll1ll_opy_ (u"ࠦࠧ᱑"))
                    result[bstack11ll1ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᱒")] = [f.strip() for f in bstack111l111ll1l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll1l11_opy_ (u"ࠨࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂ࠴࠮ࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿࠥ᱓")))
                except Exception:
                    logger.debug(bstack11ll1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡤࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡧࡴࡲࡱࠥࡨࡲࡢࡰࡦ࡬ࠥࡩ࡯࡮ࡲࡤࡶ࡮ࡹ࡯࡯࠰ࠣࡊࡦࡲ࡬ࡪࡰࡪࠤࡧࡧࡣ࡬ࠢࡷࡳࠥࡸࡥࡤࡧࡱࡸࠥࡩ࡯࡮࡯࡬ࡸࡸ࠴ࠢ᱔"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11ll1ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢ᱕")] = _1111l11111l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᱖")] = _1111l11111l_opy_(commits[:5])
            bstack111l11111ll_opy_ = set()
            bstack1111l11lll1_opy_ = []
            for commit in commits:
                logger.debug(bstack11ll1ll_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡤࡱࡰࡱ࡮ࡺ࠺ࠡࠤ᱗") + str(commit.message) + bstack11ll1ll_opy_ (u"ࠦࠧ᱘"))
                bstack111l1ll111l_opy_ = commit.author.name if commit.author else bstack11ll1ll_opy_ (u"࡛ࠧ࡮࡬ࡰࡲࡻࡳࠨ᱙")
                bstack111l11111ll_opy_.add(bstack111l1ll111l_opy_)
                bstack1111l11lll1_opy_.append({
                    bstack11ll1ll_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢᱚ"): commit.message.strip(),
                    bstack11ll1ll_opy_ (u"ࠢࡶࡵࡨࡶࠧᱛ"): bstack111l1ll111l_opy_
                })
            result[bstack11ll1ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᱜ")] = list(bstack111l11111ll_opy_)
            result[bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡏࡨࡷࡸࡧࡧࡦࡵࠥᱝ")] = bstack1111l11lll1_opy_
            result[bstack11ll1ll_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᱞ")] = bstack1111l1ll111_opy_.committed_datetime.strftime(bstack11ll1ll_opy_ (u"ࠦࠪ࡟࠭ࠦ࡯࠰ࠩࡩࠨᱟ"))
            if (not result[bstack11ll1ll_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᱠ")] or result[bstack11ll1ll_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᱡ")].strip() == bstack11ll1ll_opy_ (u"ࠢࠣᱢ")) and bstack1111l1ll111_opy_.message:
                bstack111l11111l1_opy_ = bstack1111l1ll111_opy_.message.strip().splitlines()
                result[bstack11ll1ll_opy_ (u"ࠣࡲࡵࡘ࡮ࡺ࡬ࡦࠤᱣ")] = bstack111l11111l1_opy_[0] if bstack111l11111l1_opy_ else bstack11ll1ll_opy_ (u"ࠤࠥᱤ")
                if len(bstack111l11111l1_opy_) > 2:
                    result[bstack11ll1ll_opy_ (u"ࠥࡴࡷࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠥᱥ")] = bstack11ll1ll_opy_ (u"ࠫࡡࡴࠧᱦ").join(bstack111l11111l1_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11ll1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡆࡏࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࠬ࡫ࡵ࡬ࡥࡧࡵ࠾ࠥࢁࡽࠪ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᱧ").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _1111ll1ll11_opy_(result)
    ]
    return filtered_results
def _1111ll1ll11_opy_(result):
    bstack11ll1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡦ࡮ࡳࡩࡷࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡦࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡴࡷ࡯ࡸࠥ࡯ࡳࠡࡸࡤࡰ࡮ࡪࠠࠩࡰࡲࡲ࠲࡫࡭ࡱࡶࡼࠤ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠣࡥࡳࡪࠠࡢࡷࡷ࡬ࡴࡸࡳࠪ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᱨ")
    return (
        isinstance(result.get(bstack11ll1ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᱩ"), None), list)
        and len(result[bstack11ll1ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᱪ")]) > 0
        and isinstance(result.get(bstack11ll1ll_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᱫ"), None), list)
        and len(result[bstack11ll1ll_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦᱬ")]) > 0
    )
def _1111ll1l111_opy_(repo):
    bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤ࡙ࡸࡹࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡪࡨࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡵࡩࡵࡵࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡪࡤࡶࡩࡩ࡯ࡥࡧࡧࠤࡳࡧ࡭ࡦࡵࠣࡥࡳࡪࠠࡸࡱࡵ࡯ࠥࡽࡩࡵࡪࠣࡥࡱࡲࠠࡗࡅࡖࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡷࡹ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡮࡬ࠠࡱࡱࡶࡷ࡮ࡨ࡬ࡦ࠮ࠣࡩࡱࡹࡥࠡࡐࡲࡲࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᱭ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l111l111_opy_ = origin.refs[bstack11ll1ll_opy_ (u"ࠬࡎࡅࡂࡆࠪᱮ")]
            target = bstack111l111l111_opy_.reference.name
            if target.startswith(bstack11ll1ll_opy_ (u"࠭࡯ࡳ࡫ࡪ࡭ࡳ࠵ࠧᱯ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11ll1ll_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨᱰ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l11111l_opy_(commits):
    bstack11ll1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡦࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᱱ")
    bstack111l111ll1l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1l1111l_opy_ in diff:
                        if bstack111l1l1111l_opy_.a_path:
                            bstack111l111ll1l_opy_.add(bstack111l1l1111l_opy_.a_path)
                        if bstack111l1l1111l_opy_.b_path:
                            bstack111l111ll1l_opy_.add(bstack111l1l1111l_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l111ll1l_opy_)
def bstack1111lllll1l_opy_(bstack1111ll1llll_opy_):
    bstack111l1l1ll11_opy_ = bstack111l1l11lll_opy_(bstack1111ll1llll_opy_)
    if bstack111l1l1ll11_opy_ and bstack111l1l1ll11_opy_ > bstack11l11llll1l_opy_:
        bstack111l1l1ll1l_opy_ = bstack111l1l1ll11_opy_ - bstack11l11llll1l_opy_
        bstack1111lllll11_opy_ = bstack1111ll1l11l_opy_(bstack1111ll1llll_opy_[bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᱲ")], bstack111l1l1ll1l_opy_)
        bstack1111ll1llll_opy_[bstack11ll1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᱳ")] = bstack1111lllll11_opy_
        logger.info(bstack11ll1ll_opy_ (u"࡙ࠦ࡮ࡥࠡࡥࡲࡱࡲ࡯ࡴࠡࡪࡤࡷࠥࡨࡥࡦࡰࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩ࠴ࠠࡔ࡫ࡽࡩࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࠡࡣࡩࡸࡪࡸࠠࡵࡴࡸࡲࡨࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡼࡿࠣࡏࡇࠨᱴ")
                    .format(bstack111l1l11lll_opy_(bstack1111ll1llll_opy_) / 1024))
    return bstack1111ll1llll_opy_
def bstack111l1l11lll_opy_(json_data):
    try:
        if json_data:
            bstack1111l111l11_opy_ = json.dumps(json_data)
            bstack111l1l111l1_opy_ = sys.getsizeof(bstack1111l111l11_opy_)
            return bstack111l1l111l1_opy_
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤࡨࡧ࡬ࡤࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡶ࡭ࡿ࡫ࠠࡰࡨࠣࡎࡘࡕࡎࠡࡱࡥ࡮ࡪࡩࡴ࠻ࠢࡾࢁࠧᱵ").format(e))
    return -1
def bstack1111ll1l11l_opy_(field, bstack1111l111l1l_opy_):
    try:
        bstack1111l1111ll_opy_ = len(bytes(bstack11l1l11111l_opy_, bstack11ll1ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᱶ")))
        bstack1111l1l1lll_opy_ = bytes(field, bstack11ll1ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᱷ"))
        bstack111l111llll_opy_ = len(bstack1111l1l1lll_opy_)
        bstack1111ll11l1l_opy_ = ceil(bstack111l111llll_opy_ - bstack1111l111l1l_opy_ - bstack1111l1111ll_opy_)
        if bstack1111ll11l1l_opy_ > 0:
            bstack111l1l1l1ll_opy_ = bstack1111l1l1lll_opy_[:bstack1111ll11l1l_opy_].decode(bstack11ll1ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᱸ"), errors=bstack11ll1ll_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࠩᱹ")) + bstack11l1l11111l_opy_
            return bstack111l1l1l1ll_opy_
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩࡦ࡮ࡧ࠰ࠥࡴ࡯ࡵࡪ࡬ࡲ࡬ࠦࡷࡢࡵࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩࠦࡨࡦࡴࡨ࠾ࠥࢁࡽࠣᱺ").format(e))
    return field
def bstack11l1llll11_opy_():
    env = os.environ
    if (bstack11ll1ll_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤᱻ") in env and len(env[bstack11ll1ll_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᱼ")]) > 0) or (
            bstack11ll1ll_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧᱽ") in env and len(env[bstack11ll1ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨ᱾")]) > 0):
        return {
            bstack11ll1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᱿"): bstack11ll1ll_opy_ (u"ࠤࡍࡩࡳࡱࡩ࡯ࡵࠥᲀ"),
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲁ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᲂ")),
            bstack11ll1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲃ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡊࡐࡄࡢࡒࡆࡓࡅࠣᲄ")),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲅ"): env.get(bstack11ll1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲆ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠤࡆࡍࠧᲇ")) == bstack11ll1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᲈ") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡇࡎࠨᲉ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲊ"): bstack11ll1ll_opy_ (u"ࠨࡃࡪࡴࡦࡰࡪࡉࡉࠣ᲋"),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᲌"): env.get(bstack11ll1ll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᲍")),
            bstack11ll1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᲎"): env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡎࡔࡈࠢ᲏")),
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲐ"): env.get(bstack11ll1ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࠣᲑ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠨࡃࡊࠤᲒ")) == bstack11ll1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧᲓ") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࠣᲔ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲕ"): bstack11ll1ll_opy_ (u"ࠥࡘࡷࡧࡶࡪࡵࠣࡇࡎࠨᲖ"),
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲗ"): env.get(bstack11ll1ll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣ࡜ࡋࡂࡠࡗࡕࡐࠧᲘ")),
            bstack11ll1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲙ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᲚ")),
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲛ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲜ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡎࠨᲝ")) == bstack11ll1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᲞ") and env.get(bstack11ll1ll_opy_ (u"ࠧࡉࡉࡠࡐࡄࡑࡊࠨᲟ")) == bstack11ll1ll_opy_ (u"ࠨࡣࡰࡦࡨࡷ࡭࡯ࡰࠣᲠ"):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲡ"): bstack11ll1ll_opy_ (u"ࠣࡅࡲࡨࡪࡹࡨࡪࡲࠥᲢ"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲣ"): None,
            bstack11ll1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲤ"): None,
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲥ"): None
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡕࡅࡓࡉࡈࠣᲦ")) and env.get(bstack11ll1ll_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡆࡓࡒࡓࡉࡕࠤᲧ")):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲨ"): bstack11ll1ll_opy_ (u"ࠣࡄ࡬ࡸࡧࡻࡣ࡬ࡧࡷࠦᲩ"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲪ"): env.get(bstack11ll1ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡇࡊࡖࡢࡌ࡙࡚ࡐࡠࡑࡕࡍࡌࡏࡎࠣᲫ")),
            bstack11ll1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲬ"): None,
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲭ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲮ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡋࠥᲯ")) == bstack11ll1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᲰ") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠤࡇࡖࡔࡔࡅࠣᲱ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᲲ"): bstack11ll1ll_opy_ (u"ࠦࡉࡸ࡯࡯ࡧࠥᲳ"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲴ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡑࡏࡎࡌࠤᲵ")),
            bstack11ll1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲶ"): None,
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲷ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲸ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡎࠨᲹ")) == bstack11ll1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᲺ") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࠣ᲻"))):
        return {
            bstack11ll1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᲼"): bstack11ll1ll_opy_ (u"ࠢࡔࡧࡰࡥࡵ࡮࡯ࡳࡧࠥᲽ"),
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲾ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡕࡒࡈࡃࡑࡍ࡟ࡇࡔࡊࡑࡑࡣ࡚ࡘࡌࠣᲿ")),
            bstack11ll1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳀"): env.get(bstack11ll1ll_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ᳁")),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳂"): env.get(bstack11ll1ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡉࡅࠤ᳃"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡋࠥ᳄")) == bstack11ll1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨ᳅") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠤࡊࡍ࡙ࡒࡁࡃࡡࡆࡍࠧ᳆"))):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳇"): bstack11ll1ll_opy_ (u"ࠦࡌ࡯ࡴࡍࡣࡥࠦ᳈"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳉"): env.get(bstack11ll1ll_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡕࡓࡎࠥ᳊")),
            bstack11ll1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳋"): env.get(bstack11ll1ll_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨ᳌")),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳍"): env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡍࡉࠨ᳎"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠦࡈࡏࠢ᳏")) == bstack11ll1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥ᳐") and bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࠤ᳑"))):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳒"): bstack11ll1ll_opy_ (u"ࠣࡄࡸ࡭ࡱࡪ࡫ࡪࡶࡨࠦ᳓"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰ᳔ࠧ"): env.get(bstack11ll1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳕")),
            bstack11ll1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳖"): env.get(bstack11ll1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡎࡄࡆࡊࡒ᳗ࠢ")) or env.get(bstack11ll1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤ᳘")),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳙"): env.get(bstack11ll1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᳚"))
        }
    if bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦ᳛"))):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥ᳜ࠣ"): bstack11ll1ll_opy_ (u"࡛ࠦ࡯ࡳࡶࡣ࡯ࠤࡘࡺࡵࡥ࡫ࡲࠤ࡙࡫ࡡ࡮ࠢࡖࡩࡷࡼࡩࡤࡧࡶ᳝ࠦ"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬᳞ࠣ"): bstack11ll1ll_opy_ (u"ࠨࡻࡾࡽࢀ᳟ࠦ").format(env.get(bstack11ll1ll_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪ᳠")), env.get(bstack11ll1ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙ࡏࡄࠨ᳡"))),
            bstack11ll1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨ᳢ࠦ"): env.get(bstack11ll1ll_opy_ (u"ࠥࡗ࡞࡙ࡔࡆࡏࡢࡈࡊࡌࡉࡏࡋࡗࡍࡔࡔࡉࡅࠤ᳣")),
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳤ࠥ"): env.get(bstack11ll1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈ᳥ࠧ"))
        }
    if bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒ᳦ࠣ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩ᳧ࠧ"): bstack11ll1ll_opy_ (u"ࠣࡃࡳࡴࡻ࡫ࡹࡰࡴ᳨ࠥ"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᳩ"): bstack11ll1ll_opy_ (u"ࠥࡿࢂ࠵ࡰࡳࡱ࡭ࡩࡨࡺ࠯ࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠤᳪ").format(env.get(bstack11ll1ll_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡕࡓࡎࠪᳫ")), env.get(bstack11ll1ll_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡂࡅࡆࡓ࡚ࡔࡔࡠࡐࡄࡑࡊ࠭ᳬ")), env.get(bstack11ll1ll_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡒࡕࡓࡏࡋࡃࡕࡡࡖࡐ࡚ࡍ᳭ࠧ")), env.get(bstack11ll1ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫᳮ"))),
            bstack11ll1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᳯ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᳰ")),
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᳱ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᳲ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠧࡇ࡚ࡖࡔࡈࡣࡍ࡚ࡔࡑࡡࡘࡗࡊࡘ࡟ࡂࡉࡈࡒ࡙ࠨᳳ")) and env.get(bstack11ll1ll_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣ᳴")):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᳵ"): bstack11ll1ll_opy_ (u"ࠣࡃࡽࡹࡷ࡫ࠠࡄࡋࠥᳶ"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳷"): bstack11ll1ll_opy_ (u"ࠥࡿࢂࢁࡽ࠰ࡡࡥࡹ࡮ࡲࡤ࠰ࡴࡨࡷࡺࡲࡴࡴࡁࡥࡹ࡮ࡲࡤࡊࡦࡀࡿࢂࠨ᳸").format(env.get(bstack11ll1ll_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧ᳹")), env.get(bstack11ll1ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࠪᳺ")), env.get(bstack11ll1ll_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭᳻"))),
            bstack11ll1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳼"): env.get(bstack11ll1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ᳽")),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳾"): env.get(bstack11ll1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ᳿"))
        }
    if any([env.get(bstack11ll1ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᴀ")), env.get(bstack11ll1ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡔࡈࡗࡔࡒࡖࡆࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᴁ")), env.get(bstack11ll1ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᴂ"))]):
        return {
            bstack11ll1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴃ"): bstack11ll1ll_opy_ (u"ࠣࡃ࡚ࡗࠥࡉ࡯ࡥࡧࡅࡹ࡮ࡲࡤࠣᴄ"),
            bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴅ"): env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡐࡖࡄࡏࡍࡈࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᴆ")),
            bstack11ll1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴇ"): env.get(bstack11ll1ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴈ")),
            bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴉ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴊ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᴋ")):
        return {
            bstack11ll1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴌ"): bstack11ll1ll_opy_ (u"ࠥࡆࡦࡳࡢࡰࡱࠥᴍ"),
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴎ"): env.get(bstack11ll1ll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡖࡪࡹࡵ࡭ࡶࡶ࡙ࡷࡲࠢᴏ")),
            bstack11ll1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴐ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡴࡪࡲࡶࡹࡐ࡯ࡣࡐࡤࡱࡪࠨᴑ")),
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴒ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᴓ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࠦᴔ")) or env.get(bstack11ll1ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨᴕ")):
        return {
            bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴖ"): bstack11ll1ll_opy_ (u"ࠨࡗࡦࡴࡦ࡯ࡪࡸࠢᴗ"),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴘ"): env.get(bstack11ll1ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᴙ")),
            bstack11ll1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴚ"): bstack11ll1ll_opy_ (u"ࠥࡑࡦ࡯࡮ࠡࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠥᴛ") if env.get(bstack11ll1ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨᴜ")) else None,
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴝ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡈࡋࡗࡣࡈࡕࡍࡎࡋࡗࠦᴞ"))
        }
    if any([env.get(bstack11ll1ll_opy_ (u"ࠢࡈࡅࡓࡣࡕࡘࡏࡋࡇࡆࡘࠧᴟ")), env.get(bstack11ll1ll_opy_ (u"ࠣࡉࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᴠ")), env.get(bstack11ll1ll_opy_ (u"ࠤࡊࡓࡔࡍࡌࡆࡡࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᴡ"))]):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᴢ"): bstack11ll1ll_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡈࡲ࡯ࡶࡦࠥᴣ"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴤ"): None,
            bstack11ll1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴥ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡑࡔࡒࡎࡊࡉࡔࡠࡋࡇࠦᴦ")),
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴧ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴨ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࠨᴩ")):
        return {
            bstack11ll1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴪ"): bstack11ll1ll_opy_ (u"࡙ࠧࡨࡪࡲࡳࡥࡧࡲࡥࠣᴫ"),
            bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴬ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᴭ")),
            bstack11ll1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴮ"): bstack11ll1ll_opy_ (u"ࠤࡍࡳࡧࠦࠣࡼࡿࠥᴯ").format(env.get(bstack11ll1ll_opy_ (u"ࠪࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉ࠭ᴰ"))) if env.get(bstack11ll1ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᴱ")) else None,
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴲ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᴳ"))
        }
    if bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠢࡏࡇࡗࡐࡎࡌ࡙ࠣᴴ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᴵ"): bstack11ll1ll_opy_ (u"ࠤࡑࡩࡹࡲࡩࡧࡻࠥᴶ"),
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴷ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡉࡋࡐࡍࡑ࡜ࡣ࡚ࡘࡌࠣᴸ")),
            bstack11ll1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴹ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡓࡊࡖࡈࡣࡓࡇࡍࡆࠤᴺ")),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴻ"): env.get(bstack11ll1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴼ"))
        }
    if bstack11l1ll11l_opy_(env.get(bstack11ll1ll_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡄࡇ࡙ࡏࡏࡏࡕࠥᴽ"))):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᴾ"): bstack11ll1ll_opy_ (u"ࠦࡌ࡯ࡴࡉࡷࡥࠤࡆࡩࡴࡪࡱࡱࡷࠧᴿ"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵀ"): bstack11ll1ll_opy_ (u"ࠨࡻࡾ࠱ࡾࢁ࠴ࡧࡣࡵ࡫ࡲࡲࡸ࠵ࡲࡶࡰࡶ࠳ࢀࢃࠢᵁ").format(env.get(bstack11ll1ll_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡖࡔࡏࠫᵂ")), env.get(bstack11ll1ll_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡈࡔࡔ࡙ࡉࡕࡑࡕ࡝ࠬᵃ")), env.get(bstack11ll1ll_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠩᵄ"))),
            bstack11ll1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᵅ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣ࡜ࡕࡒࡌࡈࡏࡓ࡜ࠨᵆ")),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵇ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉࠨᵈ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡋࠥᵉ")) == bstack11ll1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᵊ") and env.get(bstack11ll1ll_opy_ (u"ࠤ࡙ࡉࡗࡉࡅࡍࠤᵋ")) == bstack11ll1ll_opy_ (u"ࠥ࠵ࠧᵌ"):
        return {
            bstack11ll1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵍ"): bstack11ll1ll_opy_ (u"ࠧ࡜ࡥࡳࡥࡨࡰࠧᵎ"),
            bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵏ"): bstack11ll1ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࡼࡿࠥᵐ").format(env.get(bstack11ll1ll_opy_ (u"ࠨࡘࡈࡖࡈࡋࡌࡠࡗࡕࡐࠬᵑ"))),
            bstack11ll1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᵒ"): None,
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵓ"): None,
        }
    if env.get(bstack11ll1ll_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡖࡆࡔࡖࡍࡔࡔࠢᵔ")):
        return {
            bstack11ll1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᵕ"): bstack11ll1ll_opy_ (u"ࠨࡔࡦࡣࡰࡧ࡮ࡺࡹࠣᵖ"),
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᵗ"): None,
            bstack11ll1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵘ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣࡕࡘࡏࡋࡇࡆࡘࡤࡔࡁࡎࡇࠥᵙ")),
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵚ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᵛ"))
        }
    if any([env.get(bstack11ll1ll_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࠣᵜ")), env.get(bstack11ll1ll_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡖࡑࠨᵝ")), env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠧᵞ")), env.get(bstack11ll1ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡙ࡋࡁࡎࠤᵟ"))]):
        return {
            bstack11ll1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᵠ"): bstack11ll1ll_opy_ (u"ࠥࡇࡴࡴࡣࡰࡷࡵࡷࡪࠨᵡ"),
            bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᵢ"): None,
            bstack11ll1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᵣ"): env.get(bstack11ll1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᵤ")) or None,
            bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵥ"): env.get(bstack11ll1ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᵦ"), 0)
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᵧ")):
        return {
            bstack11ll1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᵨ"): bstack11ll1ll_opy_ (u"ࠦࡌࡵࡃࡅࠤᵩ"),
            bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵪ"): None,
            bstack11ll1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᵫ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᵬ")),
            bstack11ll1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵭ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡊࡓࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡄࡑࡘࡒ࡙ࡋࡒࠣᵮ"))
        }
    if env.get(bstack11ll1ll_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᵯ")):
        return {
            bstack11ll1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵰ"): bstack11ll1ll_opy_ (u"ࠧࡉ࡯ࡥࡧࡉࡶࡪࡹࡨࠣᵱ"),
            bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵲ"): env.get(bstack11ll1ll_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᵳ")),
            bstack11ll1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵴ"): env.get(bstack11ll1ll_opy_ (u"ࠤࡆࡊࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᵵ")),
            bstack11ll1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵶ"): env.get(bstack11ll1ll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᵷ"))
        }
    return {bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵸ"): None}
def get_host_info():
    return {
        bstack11ll1ll_opy_ (u"ࠨࡨࡰࡵࡷࡲࡦࡳࡥࠣᵹ"): platform.node(),
        bstack11ll1ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤᵺ"): platform.system(),
        bstack11ll1ll_opy_ (u"ࠣࡶࡼࡴࡪࠨᵻ"): platform.machine(),
        bstack11ll1ll_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥᵼ"): platform.version(),
        bstack11ll1ll_opy_ (u"ࠥࡥࡷࡩࡨࠣᵽ"): platform.architecture()[0]
    }
def bstack1111lll1l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111lll1l1l_opy_():
    if bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬᵾ")):
        return bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵿ")
    return bstack11ll1ll_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠬᶀ")
def bstack1111l1ll1l1_opy_(driver):
    info = {
        bstack11ll1ll_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᶁ"): driver.capabilities,
        bstack11ll1ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬᶂ"): driver.session_id,
        bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᶃ"): driver.capabilities.get(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᶄ"), None),
        bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᶅ"): driver.capabilities.get(bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᶆ"), None),
        bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨᶇ"): driver.capabilities.get(bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᶈ"), None),
        bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᶉ"):driver.capabilities.get(bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᶊ"), None),
    }
    if bstack1111lll1l1l_opy_() == bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᶋ"):
        if bstack1l11111ll_opy_():
            info[bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᶌ")] = bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᶍ")
        elif driver.capabilities.get(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᶎ"), {}).get(bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᶏ"), False):
            info[bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᶐ")] = bstack11ll1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᶑ")
        else:
            info[bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᶒ")] = bstack11ll1ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᶓ")
    return info
def bstack1l11111ll_opy_():
    if bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᶔ")):
        return True
    if bstack11l1ll11l_opy_(os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧᶕ"), None)):
        return True
    return False
def bstack11ll11ll1l_opy_(bstack1111ll11111_opy_, url, data, config):
    headers = config.get(bstack11ll1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᶖ"), None)
    proxies = bstack11l111l11_opy_(config, url)
    auth = config.get(bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᶗ"), None)
    response = requests.request(
            bstack1111ll11111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1111lllll1_opy_(bstack1lll11l111_opy_, size):
    bstack1l11ll11l1_opy_ = []
    while len(bstack1lll11l111_opy_) > size:
        bstack11l1l1ll1_opy_ = bstack1lll11l111_opy_[:size]
        bstack1l11ll11l1_opy_.append(bstack11l1l1ll1_opy_)
        bstack1lll11l111_opy_ = bstack1lll11l111_opy_[size:]
    bstack1l11ll11l1_opy_.append(bstack1lll11l111_opy_)
    return bstack1l11ll11l1_opy_
def bstack111l11ll1l1_opy_(message, bstack111l11ll11l_opy_=False):
    os.write(1, bytes(message, bstack11ll1ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᶘ")))
    os.write(1, bytes(bstack11ll1ll_opy_ (u"ࠪࡠࡳ࠭ᶙ"), bstack11ll1ll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᶚ")))
    if bstack111l11ll11l_opy_:
        with open(bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡵ࠱࠲ࡻ࠰ࠫᶛ") + os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᶜ")] + bstack11ll1ll_opy_ (u"ࠧ࠯࡮ࡲ࡫ࠬᶝ"), bstack11ll1ll_opy_ (u"ࠨࡣࠪᶞ")) as f:
            f.write(message + bstack11ll1ll_opy_ (u"ࠩ࡟ࡲࠬᶟ"))
def bstack1lll11lll11_opy_():
    return os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᶠ")].lower() == bstack11ll1ll_opy_ (u"ࠫࡹࡸࡵࡦࠩᶡ")
def bstack1ll111ll_opy_():
    return bstack1llll1l1_opy_().replace(tzinfo=None).isoformat() + bstack11ll1ll_opy_ (u"ࠬࡠࠧᶢ")
def bstack111l1l11ll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll1ll_opy_ (u"࡚࠭ࠨᶣ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll1ll_opy_ (u"࡛ࠧࠩᶤ")))).total_seconds() * 1000
def bstack111l11lll1l_opy_(timestamp):
    return bstack1111l1l1ll1_opy_(timestamp).isoformat() + bstack11ll1ll_opy_ (u"ࠨ࡜ࠪᶥ")
def bstack1111l1ll11l_opy_(bstack111l1111111_opy_):
    date_format = bstack11ll1ll_opy_ (u"ࠩࠨ࡝ࠪࡳࠥࡥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠧᶦ")
    bstack1111ll111ll_opy_ = datetime.datetime.strptime(bstack111l1111111_opy_, date_format)
    return bstack1111ll111ll_opy_.isoformat() + bstack11ll1ll_opy_ (u"ࠪ࡞ࠬᶧ")
def bstack111l11lll11_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᶨ")
    else:
        return bstack11ll1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᶩ")
def bstack11l1ll11l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫᶪ")
def bstack111l11ll111_opy_(val):
    return val.__str__().lower() == bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ᶫ")
def error_handler(bstack1111l11l1l1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111l11l1l1_opy_ as e:
                print(bstack11ll1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣᶬ").format(func.__name__, bstack1111l11l1l1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l1l1l11l_opy_(bstack1111ll1l1l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111ll1l1l1_opy_(cls, *args, **kwargs)
            except bstack1111l11l1l1_opy_ as e:
                print(bstack11ll1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᶭ").format(bstack1111ll1l1l1_opy_.__name__, bstack1111l11l1l1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l1l1l11l_opy_
    else:
        return decorator
def bstack1ll1llll1l_opy_(bstack1111l1ll_opy_):
    if os.getenv(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᶮ")) is not None:
        return bstack11l1ll11l_opy_(os.getenv(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᶯ")))
    if bstack11ll1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶰ") in bstack1111l1ll_opy_ and bstack111l11ll111_opy_(bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶱ")]):
        return False
    if bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶲ") in bstack1111l1ll_opy_ and bstack111l11ll111_opy_(bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶳ")]):
        return False
    return True
def bstack1llllll1l1_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111ll1ll1l_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤᶴ"), None)
        return bstack1111ll1ll1l_opy_ is None or bstack1111ll1ll1l_opy_ == bstack11ll1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᶵ")
    except Exception as e:
        return False
def bstack111l1l1111_opy_(hub_url, CONFIG):
    if bstack11llll1111_opy_() <= version.parse(bstack11ll1ll_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫᶶ")):
        if hub_url:
            return bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᶷ") + hub_url + bstack11ll1ll_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥᶸ")
        return bstack1l1l1lllll_opy_
    if hub_url:
        return bstack11ll1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᶹ") + hub_url + bstack11ll1ll_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤᶺ")
    return bstack11lll111ll_opy_
def bstack111l111l1ll_opy_():
    return isinstance(os.getenv(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨᶻ")), str)
def bstack1111l1111_opy_(url):
    return urlparse(url).hostname
def bstack1l111ll1l_opy_(hostname):
    for bstack11l1ll1111_opy_ in bstack11lll111l_opy_:
        regex = re.compile(bstack11l1ll1111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l1llll1l1_opy_(bstack1111l111lll_opy_, file_name, logger):
    bstack1l111lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠪࢂࠬᶼ")), bstack1111l111lll_opy_)
    try:
        if not os.path.exists(bstack1l111lll11_opy_):
            os.makedirs(bstack1l111lll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠫࢃ࠭ᶽ")), bstack1111l111lll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll1ll_opy_ (u"ࠬࡽࠧᶾ")):
                pass
            with open(file_path, bstack11ll1ll_opy_ (u"ࠨࡷࠬࠤᶿ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1llll1111l_opy_.format(str(e)))
def bstack11l1lllll11_opy_(file_name, key, value, logger):
    file_path = bstack11l1llll1l1_opy_(bstack11ll1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ᷀"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1llll1l1_opy_ = json.load(open(file_path, bstack11ll1ll_opy_ (u"ࠨࡴࡥࠫ᷁")))
        else:
            bstack1l1llll1l1_opy_ = {}
        bstack1l1llll1l1_opy_[key] = value
        with open(file_path, bstack11ll1ll_opy_ (u"ࠤࡺ࠯᷂ࠧ")) as outfile:
            json.dump(bstack1l1llll1l1_opy_, outfile)
def bstack1ll1l1lll1_opy_(file_name, logger):
    file_path = bstack11l1llll1l1_opy_(bstack11ll1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ᷃"), file_name, logger)
    bstack1l1llll1l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll1ll_opy_ (u"ࠫࡷ࠭᷄")) as bstack1l11lllll1_opy_:
            bstack1l1llll1l1_opy_ = json.load(bstack1l11lllll1_opy_)
    return bstack1l1llll1l1_opy_
def bstack1l1l111ll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫࠺ࠡࠩ᷅") + file_path + bstack11ll1ll_opy_ (u"࠭ࠠࠨ᷆") + str(e))
def bstack11llll1111_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll1ll_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤ᷇")
def bstack1l11lllll_opy_(config):
    if bstack11ll1ll_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ᷈") in config:
        del (config[bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ᷉")])
        return False
    if bstack11llll1111_opy_() < version.parse(bstack11ll1ll_opy_ (u"ࠪ࠷࠳࠺࠮࠱᷊ࠩ")):
        return False
    if bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪ᷋")):
        return True
    if bstack11ll1ll_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ᷌") in config and config[bstack11ll1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭᷍")] is False:
        return False
    else:
        return True
def bstack1l1111111l_opy_(args_list, bstack111l11ll1ll_opy_):
    index = -1
    for value in bstack111l11ll1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111ll111l1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111ll111l1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l11l11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l11l11l_opy_ = bstack1l11l11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11ll1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪ᷎ࠧ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᷏"), exception=exception)
    def bstack1111111l11_opy_(self):
        if self.result != bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ᷐ࠩ"):
            return None
        if isinstance(self.exception_type, str) and bstack11ll1ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ᷑") in self.exception_type:
            return bstack11ll1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧ᷒")
        return bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᷓ")
    def bstack1111l111111_opy_(self):
        if self.result != bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᷔ"):
            return None
        if self.bstack1l11l11l_opy_:
            return self.bstack1l11l11l_opy_
        return bstack111l11l1111_opy_(self.exception)
def bstack111l11l1111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l1l1111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l1l1ll1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11l11ll1l1_opy_(config, logger):
    try:
        import playwright
        bstack1111l1l1l1l_opy_ = playwright.__file__
        bstack1111l1ll1ll_opy_ = os.path.split(bstack1111l1l1l1l_opy_)
        bstack111l11llll1_opy_ = bstack1111l1ll1ll_opy_[0] + bstack11ll1ll_opy_ (u"ࠧ࠰ࡦࡵ࡭ࡻ࡫ࡲ࠰ࡲࡤࡧࡰࡧࡧࡦ࠱࡯࡭ࡧ࠵ࡣ࡭࡫࠲ࡧࡱ࡯࠮࡫ࡵࠪᷕ")
        os.environ[bstack11ll1ll_opy_ (u"ࠨࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜ࠫᷖ")] = bstack1l111ll1ll_opy_(config)
        with open(bstack111l11llll1_opy_, bstack11ll1ll_opy_ (u"ࠩࡵࠫᷗ")) as f:
            file_content = f.read()
            bstack111l111l11l_opy_ = bstack11ll1ll_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩᷘ")
            bstack1111lll11ll_opy_ = file_content.find(bstack111l111l11l_opy_)
            if bstack1111lll11ll_opy_ == -1:
              process = subprocess.Popen(bstack11ll1ll_opy_ (u"ࠦࡳࡶ࡭ࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠣᷙ"), shell=True, cwd=bstack1111l1ll1ll_opy_[0])
              process.wait()
              bstack1111llll11l_opy_ = bstack11ll1ll_opy_ (u"ࠬࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶࠥ࠿ࠬᷚ")
              bstack1111llll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࠢࠣࠢ࡟ࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴ࡝ࠤ࠾ࠤࡨࡵ࡮ࡴࡶࠣࡿࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠡࡿࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ࠩ࠼ࠢ࡬ࡪࠥ࠮ࡰࡳࡱࡦࡩࡸࡹ࠮ࡦࡰࡹ࠲ࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠩࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠬ࠮ࡁࠠࠣࠤࠥᷛ")
              bstack111l1111ll1_opy_ = file_content.replace(bstack1111llll11l_opy_, bstack1111llll1ll_opy_)
              with open(bstack111l11llll1_opy_, bstack11ll1ll_opy_ (u"ࠧࡸࠩᷜ")) as f:
                f.write(bstack111l1111ll1_opy_)
    except Exception as e:
        logger.error(bstack1l1lll11ll_opy_.format(str(e)))
def bstack1l111111l1_opy_():
  try:
    bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᷝ"))
    bstack111l1l11111_opy_ = []
    if os.path.exists(bstack111l1l1l111_opy_):
      with open(bstack111l1l1l111_opy_) as f:
        bstack111l1l11111_opy_ = json.load(f)
      os.remove(bstack111l1l1l111_opy_)
    return bstack111l1l11111_opy_
  except:
    pass
  return []
def bstack11ll1l111_opy_(bstack1l1l1l1l11_opy_):
  try:
    bstack111l1l11111_opy_ = []
    bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᷞ"))
    if os.path.exists(bstack111l1l1l111_opy_):
      with open(bstack111l1l1l111_opy_) as f:
        bstack111l1l11111_opy_ = json.load(f)
    bstack111l1l11111_opy_.append(bstack1l1l1l1l11_opy_)
    with open(bstack111l1l1l111_opy_, bstack11ll1ll_opy_ (u"ࠪࡻࠬᷟ")) as f:
        json.dump(bstack111l1l11111_opy_, f)
  except:
    pass
def bstack1lllllll11_opy_(logger, bstack1111lll111l_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll1ll_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᷠ"), bstack11ll1ll_opy_ (u"ࠬ࠭ᷡ"))
    if test_name == bstack11ll1ll_opy_ (u"࠭ࠧᷢ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࡂࡥࡦࡢࡸࡪࡹࡴࡠࡰࡤࡱࡪ࠭ᷣ"), bstack11ll1ll_opy_ (u"ࠨࠩᷤ"))
    bstack111l1l111ll_opy_ = bstack11ll1ll_opy_ (u"ࠩ࠯ࠤࠬᷥ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111lll111l_opy_:
        bstack1l11111l1l_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᷦ"), bstack11ll1ll_opy_ (u"ࠫ࠵࠭ᷧ"))
        bstack1l1lll1l1_opy_ = {bstack11ll1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᷨ"): test_name, bstack11ll1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᷩ"): bstack111l1l111ll_opy_, bstack11ll1ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᷪ"): bstack1l11111l1l_opy_}
        bstack1111llll111_opy_ = []
        bstack1111ll11ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᷫ"))
        if os.path.exists(bstack1111ll11ll1_opy_):
            with open(bstack1111ll11ll1_opy_) as f:
                bstack1111llll111_opy_ = json.load(f)
        bstack1111llll111_opy_.append(bstack1l1lll1l1_opy_)
        with open(bstack1111ll11ll1_opy_, bstack11ll1ll_opy_ (u"ࠩࡺࠫᷬ")) as f:
            json.dump(bstack1111llll111_opy_, f)
    else:
        bstack1l1lll1l1_opy_ = {bstack11ll1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᷭ"): test_name, bstack11ll1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷮ"): bstack111l1l111ll_opy_, bstack11ll1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷯ"): str(multiprocessing.current_process().name)}
        if bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪᷰ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1lll1l1_opy_)
  except Exception as e:
      logger.warn(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡳࡽࡹ࡫ࡳࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᷱ").format(e))
def bstack1ll1l11ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫᷲ"))
    try:
      bstack1111l111ll1_opy_ = []
      bstack1l1lll1l1_opy_ = {bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᷳ"): test_name, bstack11ll1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᷴ"): error_message, bstack11ll1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ᷵"): index}
      bstack111l111ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭᷶"))
      if os.path.exists(bstack111l111ll11_opy_):
          with open(bstack111l111ll11_opy_) as f:
              bstack1111l111ll1_opy_ = json.load(f)
      bstack1111l111ll1_opy_.append(bstack1l1lll1l1_opy_)
      with open(bstack111l111ll11_opy_, bstack11ll1ll_opy_ (u"࠭ࡷࠨ᷷")) as f:
          json.dump(bstack1111l111ll1_opy_, f)
    except Exception as e:
      logger.warn(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿ᷸ࠥ").format(e))
    return
  bstack1111l111ll1_opy_ = []
  bstack1l1lll1l1_opy_ = {bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ᷹࠭"): test_name, bstack11ll1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ᷺"): error_message, bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ᷻"): index}
  bstack111l111ll11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ᷼"))
  lock_file = bstack111l111ll11_opy_ + bstack11ll1ll_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮᷽ࠫ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l111ll11_opy_):
          with open(bstack111l111ll11_opy_, bstack11ll1ll_opy_ (u"࠭ࡲࠨ᷾")) as f:
              content = f.read().strip()
              if content:
                  bstack1111l111ll1_opy_ = json.load(open(bstack111l111ll11_opy_))
      bstack1111l111ll1_opy_.append(bstack1l1lll1l1_opy_)
      with open(bstack111l111ll11_opy_, bstack11ll1ll_opy_ (u"ࠧࡸ᷿ࠩ")) as f:
          json.dump(bstack1111l111ll1_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪ࠾ࠥࢁࡽࠣḀ").format(e))
def bstack1l11ll1lll_opy_(bstack1ll1ll1ll_opy_, name, logger):
  try:
    bstack1l1lll1l1_opy_ = {bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧḁ"): name, bstack11ll1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩḂ"): bstack1ll1ll1ll_opy_, bstack11ll1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪḃ"): str(threading.current_thread()._name)}
    return bstack1l1lll1l1_opy_
  except Exception as e:
    logger.warn(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤḄ").format(e))
  return
def bstack111l1l11l1l_opy_():
    return platform.system() == bstack11ll1ll_opy_ (u"࠭ࡗࡪࡰࡧࡳࡼࡹࠧḅ")
def bstack111l1l1lll_opy_(bstack1111l1llll1_opy_, config, logger):
    bstack111l11lllll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111l1llll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡲࡴࡦࡴࠣࡧࡴࡴࡦࡪࡩࠣ࡯ࡪࡿࡳࠡࡤࡼࠤࡷ࡫ࡧࡦࡺࠣࡱࡦࡺࡣࡩ࠼ࠣࡿࢂࠨḆ").format(e))
    return bstack111l11lllll_opy_
def bstack11l1l11llll_opy_(bstack111l11l1l1l_opy_, bstack1111llll1l1_opy_):
    bstack111l11l11ll_opy_ = version.parse(bstack111l11l1l1l_opy_)
    bstack1111ll11lll_opy_ = version.parse(bstack1111llll1l1_opy_)
    if bstack111l11l11ll_opy_ > bstack1111ll11lll_opy_:
        return 1
    elif bstack111l11l11ll_opy_ < bstack1111ll11lll_opy_:
        return -1
    else:
        return 0
def bstack1llll1l1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l1l1ll1_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll11l11_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11llllll1l_opy_(options, framework, config, bstack1ll11ll1l1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11ll1ll_opy_ (u"ࠨࡩࡨࡸࠬḇ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l111l1l11_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪḈ"))
    bstack1111l11ll1l_opy_ = True
    bstack1lll111lll_opy_ = os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨḉ")]
    bstack1l1111lllll_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫḊ"), False)
    if bstack1l1111lllll_opy_:
        bstack1l1l11l1ll1_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬḋ"), {})
        bstack1l1l11l1ll1_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩḌ")] = os.getenv(bstack11ll1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬḍ"))
        bstack1111l11ll11_opy_ = json.loads(os.getenv(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩḎ"), bstack11ll1ll_opy_ (u"ࠩࡾࢁࠬḏ"))).get(bstack11ll1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫḐ"))
    if bstack111l11ll111_opy_(caps.get(bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡗ࠴ࡅࠪḑ"))) or bstack111l11ll111_opy_(caps.get(bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬḒ"))):
        bstack1111l11ll1l_opy_ = False
    if bstack1l11lllll_opy_({bstack11ll1ll_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨḓ"): bstack1111l11ll1l_opy_}):
        bstack1l111l1l11_opy_ = bstack1l111l1l11_opy_ or {}
        bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩḔ")] = bstack1111ll11l11_opy_(framework)
        bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪḕ")] = bstack1lll11lll11_opy_()
        bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬḖ")] = bstack1lll111lll_opy_
        bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬḗ")] = bstack1ll11ll1l1_opy_
        if bstack1l1111lllll_opy_:
            bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫḘ")] = bstack1l1111lllll_opy_
            bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬḙ")] = bstack1l1l11l1ll1_opy_
            bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭Ḛ")][bstack11ll1ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨḛ")] = bstack1111l11ll11_opy_
        if getattr(options, bstack11ll1ll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩḜ"), None):
            options.set_capability(bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪḝ"), bstack1l111l1l11_opy_)
        else:
            options[bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫḞ")] = bstack1l111l1l11_opy_
    else:
        if getattr(options, bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬḟ"), None):
            options.set_capability(bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭Ḡ"), bstack1111ll11l11_opy_(framework))
            options.set_capability(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧḡ"), bstack1lll11lll11_opy_())
            options.set_capability(bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩḢ"), bstack1lll111lll_opy_)
            options.set_capability(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩḣ"), bstack1ll11ll1l1_opy_)
            if bstack1l1111lllll_opy_:
                options.set_capability(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨḤ"), bstack1l1111lllll_opy_)
                options.set_capability(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩḥ"), bstack1l1l11l1ll1_opy_)
                options.set_capability(bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ࠱ࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫḦ"), bstack1111l11ll11_opy_)
        else:
            options[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ḧ")] = bstack1111ll11l11_opy_(framework)
            options[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧḨ")] = bstack1lll11lll11_opy_()
            options[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩḩ")] = bstack1lll111lll_opy_
            options[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩḪ")] = bstack1ll11ll1l1_opy_
            if bstack1l1111lllll_opy_:
                options[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨḫ")] = bstack1l1111lllll_opy_
                options[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩḬ")] = bstack1l1l11l1ll1_opy_
                options[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḭ")][bstack11ll1ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ḯ")] = bstack1111l11ll11_opy_
    return options
def bstack111l1l1l1l1_opy_(ws_endpoint, framework):
    bstack1ll11ll1l1_opy_ = bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣḯ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11ll1ll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭Ḱ"))) > 1:
        ws_url = ws_endpoint.split(bstack11ll1ll_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḱ"))[0]
        if bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬḲ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111lll1lll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11ll1ll_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḳ"))[1]))
            bstack1111lll1lll_opy_ = bstack1111lll1lll_opy_ or {}
            bstack1lll111lll_opy_ = os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩḴ")]
            bstack1111lll1lll_opy_[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ḵ")] = str(framework) + str(__version__)
            bstack1111lll1lll_opy_[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧḶ")] = bstack1lll11lll11_opy_()
            bstack1111lll1lll_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩḷ")] = bstack1lll111lll_opy_
            bstack1111lll1lll_opy_[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩḸ")] = bstack1ll11ll1l1_opy_
            ws_endpoint = ws_endpoint.split(bstack11ll1ll_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḹ"))[0] + bstack11ll1ll_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḺ") + urllib.parse.quote(json.dumps(bstack1111lll1lll_opy_))
    return ws_endpoint
def bstack1lll11l1ll_opy_():
    global bstack11lll111l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11lll111l1_opy_ = BrowserType.connect
    return bstack11lll111l1_opy_
def bstack1llllllll1_opy_(framework_name):
    global bstack1lllll1ll1_opy_
    bstack1lllll1ll1_opy_ = framework_name
    return framework_name
def bstack1l1ll1llll_opy_(self, *args, **kwargs):
    global bstack11lll111l1_opy_
    try:
        global bstack1lllll1ll1_opy_
        if bstack11ll1ll_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨḻ") in kwargs:
            kwargs[bstack11ll1ll_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩḼ")] = bstack111l1l1l1l1_opy_(
                kwargs.get(bstack11ll1ll_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḽ"), None),
                bstack1lllll1ll1_opy_
            )
    except Exception as e:
        logger.error(bstack11ll1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢḾ").format(str(e)))
    return bstack11lll111l1_opy_(self, *args, **kwargs)
def bstack111l1l11l11_opy_(bstack1111llllll1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11l111l11_opy_(bstack1111llllll1_opy_, bstack11ll1ll_opy_ (u"ࠣࠤḿ"))
        if proxies and proxies.get(bstack11ll1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣṀ")):
            parsed_url = urlparse(proxies.get(bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤṁ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧṂ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨṃ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩṄ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11ll1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪṅ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l11ll11l_opy_(bstack1111llllll1_opy_):
    bstack1111lll1l11_opy_ = {
        bstack11l1l11l1ll_opy_[bstack111l1l1llll_opy_]: bstack1111llllll1_opy_[bstack111l1l1llll_opy_]
        for bstack111l1l1llll_opy_ in bstack1111llllll1_opy_
        if bstack111l1l1llll_opy_ in bstack11l1l11l1ll_opy_
    }
    bstack1111lll1l11_opy_[bstack11ll1ll_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣṆ")] = bstack111l1l11l11_opy_(bstack1111llllll1_opy_, bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤṇ")))
    bstack1111lll1111_opy_ = [element.lower() for element in bstack11l11ll111l_opy_]
    bstack1111l1lll11_opy_(bstack1111lll1l11_opy_, bstack1111lll1111_opy_)
    return bstack1111lll1l11_opy_
def bstack1111l1lll11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11ll1ll_opy_ (u"ࠥ࠮࠯࠰ࠪࠣṈ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l1lll11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l1lll11_opy_(item, keys)
def bstack1ll1l1l11l1_opy_():
    bstack1111l11l11l_opy_ = [os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡎࡒࡅࡔࡡࡇࡍࡗࠨṉ")), os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠧࢄࠢṊ")), bstack11ll1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ṋ")), os.path.join(bstack11ll1ll_opy_ (u"ࠧ࠰ࡶࡰࡴࠬṌ"), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨṍ"))]
    for path in bstack1111l11l11l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11ll1ll_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤṎ") + str(path) + bstack11ll1ll_opy_ (u"ࠥࠫࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨṏ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11ll1ll_opy_ (u"ࠦࡌ࡯ࡶࡪࡰࡪࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡩࡳࡷࠦࠧࠣṐ") + str(path) + bstack11ll1ll_opy_ (u"ࠧ࠭ࠢṑ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨṒ") + str(path) + bstack11ll1ll_opy_ (u"ࠢࠨࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡬ࡦࡹࠠࡵࡪࡨࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶ࠲ࠧṓ"))
            else:
                logger.debug(bstack11ll1ll_opy_ (u"ࠣࡅࡵࡩࡦࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࠩࠥṔ") + str(path) + bstack11ll1ll_opy_ (u"ࠤࠪࠤࡼ࡯ࡴࡩࠢࡺࡶ࡮ࡺࡥࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲ࠳ࠨṕ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11ll1ll_opy_ (u"ࠥࡓࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠢࡩࡳࡷࠦࠧࠣṖ") + str(path) + bstack11ll1ll_opy_ (u"ࠦࠬ࠴ࠢṗ"))
            return path
        except Exception as e:
            logger.debug(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡻࡰࠡࡨ࡬ࡰࡪࠦࠧࡼࡲࡤࡸ࡭ࢃࠧ࠻ࠢࠥṘ") + str(e) + bstack11ll1ll_opy_ (u"ࠨࠢṙ"))
    logger.debug(bstack11ll1ll_opy_ (u"ࠢࡂ࡮࡯ࠤࡵࡧࡴࡩࡵࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠦṚ"))
    return None
@measure(event_name=EVENTS.bstack11l1l111l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack1l1l111l1l1_opy_(binary_path, bstack1l1l1llllll_opy_, bs_config):
    logger.debug(bstack11ll1ll_opy_ (u"ࠣࡅࡸࡶࡷ࡫࡮ࡵࠢࡆࡐࡎࠦࡐࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦ࠽ࠤࢀࢃࠢṛ").format(binary_path))
    bstack1111ll1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠩࠪṜ")
    bstack1111l11llll_opy_ = {
        bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨṝ"): __version__,
        bstack11ll1ll_opy_ (u"ࠦࡴࡹࠢṞ"): platform.system(),
        bstack11ll1ll_opy_ (u"ࠧࡵࡳࡠࡣࡵࡧ࡭ࠨṟ"): platform.machine(),
        bstack11ll1ll_opy_ (u"ࠨࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠦṠ"): bstack11ll1ll_opy_ (u"ࠧ࠱ࠩṡ"),
        bstack11ll1ll_opy_ (u"ࠣࡵࡧ࡯ࡤࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠢṢ"): bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩṣ")
    }
    bstack11111lllll1_opy_(bstack1111l11llll_opy_)
    try:
        if binary_path:
            if bstack111l1l11l1l_opy_():
                bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨṤ")] = subprocess.check_output([binary_path, bstack11ll1ll_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧṥ")]).strip().decode(bstack11ll1ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫṦ"))
            else:
                bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫṧ")] = subprocess.check_output([binary_path, bstack11ll1ll_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣṨ")], stderr=subprocess.DEVNULL).strip().decode(bstack11ll1ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧṩ"))
        response = requests.request(
            bstack11ll1ll_opy_ (u"ࠩࡊࡉ࡙࠭Ṫ"),
            url=bstack11l1l1l1l1_opy_(bstack11l11ll1ll1_opy_),
            headers=None,
            auth=(bs_config[bstack11ll1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬṫ")], bs_config[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧṬ")]),
            json=None,
            params=bstack1111l11llll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11ll1ll_opy_ (u"ࠬࡻࡲ࡭ࠩṭ") in data.keys() and bstack11ll1ll_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡪ࡟ࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬṮ") in data.keys():
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡏࡧࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡤ࡬ࡲࡦࡸࡹ࠭ࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡺࡪࡸࡳࡪࡱࡱ࠾ࠥࢁࡽࠣṯ").format(bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ṱ")]))
            if bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠬṱ") in os.environ:
                logger.debug(bstack11ll1ll_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡨࡩ࡯ࡣࡵࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡢࡵࠣࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑࠦࡩࡴࠢࡶࡩࡹࠨṲ"))
                data[bstack11ll1ll_opy_ (u"ࠫࡺࡸ࡬ࠨṳ")] = os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠨṴ")]
            bstack111l111111l_opy_ = bstack111l1111l11_opy_(data[bstack11ll1ll_opy_ (u"࠭ࡵࡳ࡮ࠪṵ")], bstack1l1l1llllll_opy_)
            bstack1111ll1l1ll_opy_ = os.path.join(bstack1l1l1llllll_opy_, bstack111l111111l_opy_)
            os.chmod(bstack1111ll1l1ll_opy_, 0o777) # bstack1111ll1lll1_opy_ permission
            return bstack1111ll1l1ll_opy_
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡲࡪࡽࠠࡔࡆࡎࠤࢀࢃࠢṶ").format(e))
    return binary_path
def bstack11111lllll1_opy_(bstack1111l11llll_opy_):
    try:
        if bstack11ll1ll_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧṷ") not in bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡲࡷࠬṸ")].lower():
            return
        if os.path.exists(bstack11ll1ll_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṹ")):
            with open(bstack11ll1ll_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṺ"), bstack11ll1ll_opy_ (u"ࠧࡸࠢṻ")) as f:
                bstack111l11l1ll1_opy_ = {}
                for line in f:
                    if bstack11ll1ll_opy_ (u"ࠨ࠽ࠣṼ") in line:
                        key, value = line.rstrip().split(bstack11ll1ll_opy_ (u"ࠢ࠾ࠤṽ"), 1)
                        bstack111l11l1ll1_opy_[key] = value.strip(bstack11ll1ll_opy_ (u"ࠨࠤ࡟ࠫࠬṾ"))
                bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡧ࡭ࡸࡺࡲࡰࠩṿ")] = bstack111l11l1ll1_opy_.get(bstack11ll1ll_opy_ (u"ࠥࡍࡉࠨẀ"), bstack11ll1ll_opy_ (u"ࠦࠧẁ"))
        elif os.path.exists(bstack11ll1ll_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡥࡱࡶࡩ࡯ࡧ࠰ࡶࡪࡲࡥࡢࡵࡨࠦẂ")):
            bstack1111l11llll_opy_[bstack11ll1ll_opy_ (u"࠭ࡤࡪࡵࡷࡶࡴ࠭ẃ")] = bstack11ll1ll_opy_ (u"ࠧࡢ࡮ࡳ࡭ࡳ࡫ࠧẄ")
    except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡦ࡬ࡷࡹࡸ࡯ࠡࡱࡩࠤࡱ࡯࡮ࡶࡺࠥẅ") + e)
@measure(event_name=EVENTS.bstack11l11l1lll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack111l1111l11_opy_(bstack1111l1lll1l_opy_, bstack1111ll1111l_opy_):
    logger.debug(bstack11ll1ll_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮࠼ࠣࠦẆ") + str(bstack1111l1lll1l_opy_) + bstack11ll1ll_opy_ (u"ࠥࠦẇ"))
    zip_path = os.path.join(bstack1111ll1111l_opy_, bstack11ll1ll_opy_ (u"ࠦࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࡠࡨ࡬ࡰࡪ࠴ࡺࡪࡲࠥẈ"))
    bstack111l111111l_opy_ = bstack11ll1ll_opy_ (u"ࠬ࠭ẉ")
    with requests.get(bstack1111l1lll1l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11ll1ll_opy_ (u"ࠨࡷࡣࠤẊ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11ll1ll_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹ࠯ࠤẋ"))
    with zipfile.ZipFile(zip_path, bstack11ll1ll_opy_ (u"ࠨࡴࠪẌ")) as zip_ref:
        bstack1111lllllll_opy_ = zip_ref.namelist()
        if len(bstack1111lllllll_opy_) > 0:
            bstack111l111111l_opy_ = bstack1111lllllll_opy_[0] # bstack1111l1l11l1_opy_ bstack11l11ll1111_opy_ will be bstack1111l11l111_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111ll1111l_opy_)
        logger.debug(bstack11ll1ll_opy_ (u"ࠤࡉ࡭ࡱ࡫ࡳࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡦࡺࡷࡶࡦࡩࡴࡦࡦࠣࡸࡴࠦࠧࠣẍ") + str(bstack1111ll1111l_opy_) + bstack11ll1ll_opy_ (u"ࠥࠫࠧẎ"))
    os.remove(zip_path)
    return bstack111l111111l_opy_
def get_cli_dir():
    bstack1111l1lllll_opy_ = bstack1ll1l1l11l1_opy_()
    if bstack1111l1lllll_opy_:
        bstack1l1l1llllll_opy_ = os.path.join(bstack1111l1lllll_opy_, bstack11ll1ll_opy_ (u"ࠦࡨࡲࡩࠣẏ"))
        if not os.path.exists(bstack1l1l1llllll_opy_):
            os.makedirs(bstack1l1l1llllll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1llllll_opy_
    else:
        raise FileNotFoundError(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡩࡳࡷࠦࡴࡩࡧࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿ࠮ࠣẐ"))
def bstack1l11ll11l11_opy_(bstack1l1l1llllll_opy_):
    bstack11ll1ll_opy_ (u"ࠨࠢࠣࡉࡨࡸࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼࠤ࡮ࡴࠠࡢࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࠣࠤࠥẑ")
    bstack11111llllll_opy_ = [
        os.path.join(bstack1l1l1llllll_opy_, f)
        for f in os.listdir(bstack1l1l1llllll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1llllll_opy_, f)) and f.startswith(bstack11ll1ll_opy_ (u"ࠢࡣ࡫ࡱࡥࡷࡿ࠭ࠣẒ"))
    ]
    if len(bstack11111llllll_opy_) > 0:
        return max(bstack11111llllll_opy_, key=os.path.getmtime) # get bstack111l111l1l1_opy_ binary
    return bstack11ll1ll_opy_ (u"ࠣࠤẓ")
def bstack1111l1l1l11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111ll11l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111ll11l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111l111l11_opy_(data, keys, default=None):
    bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡖࡥ࡫࡫࡬ࡺࠢࡪࡩࡹࠦࡡࠡࡰࡨࡷࡹ࡫ࡤࠡࡸࡤࡰࡺ࡫ࠠࡧࡴࡲࡱࠥࡧࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡨࡦࡺࡡ࠻ࠢࡗ࡬ࡪࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷࠤࡹࡵࠠࡵࡴࡤࡺࡪࡸࡳࡦ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠ࡬ࡧࡼࡷ࠿ࠦࡁࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢ࡮ࡩࡾࡹ࠯ࡪࡰࡧ࡭ࡨ࡫ࡳࠡࡴࡨࡴࡷ࡫ࡳࡦࡰࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡥࡧࡩࡥࡺࡲࡴ࠻࡙ࠢࡥࡱࡻࡥࠡࡶࡲࠤࡷ࡫ࡴࡶࡴࡱࠤ࡮࡬ࠠࡵࡪࡨࠤࡵࡧࡴࡩࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡵࡩࡹࡻࡲ࡯࠼ࠣࡘ࡭࡫ࠠࡷࡣ࡯ࡹࡪࠦࡡࡵࠢࡷ࡬ࡪࠦ࡮ࡦࡵࡷࡩࡩࠦࡰࡢࡶ࡫࠰ࠥࡵࡲࠡࡦࡨࡪࡦࡻ࡬ࡵࠢ࡬ࡪࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠯ࠌࠣࠤࠥࠦࠢࠣࠤẔ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default