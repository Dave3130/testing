# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
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
from bstack_utils.constants import (bstack1lllllll1l_opy_, bstack1ll11l1lll_opy_, bstack1l111l111_opy_,
                                    bstack11l1l11l1ll_opy_, bstack11l11l11lll_opy_, bstack11l11l1lll1_opy_, bstack11l11ll1l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11ll1ll1l1_opy_, bstack1l11ll1l1_opy_
from bstack_utils.proxy import bstack1111l1l111_opy_, bstack111lll1ll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11ll1l11l1_opy_
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack1llll11l11_opy_
from browserstack_sdk._version import __version__
bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
logger = bstack11ll1l11l1_opy_.get_logger(__name__, bstack11ll1l11l1_opy_.bstack1l11l1llll1_opy_())
def bstack111l1l1111l_opy_(config):
    return config[bstack11l1111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᰚ")]
def bstack1111ll1l11l_opy_(config):
    return config[bstack11l1111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᰛ")]
def bstack111ll1llll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1l1l1ll_opy_(obj):
    values = []
    bstack11111llllll_opy_ = re.compile(bstack11l1111_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᰜ"), re.I)
    for key in obj.keys():
        if bstack11111llllll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111lll1111_opy_(config):
    tags = []
    tags.extend(bstack111l1l1l1ll_opy_(os.environ))
    tags.extend(bstack111l1l1l1ll_opy_(config))
    return tags
def bstack1111l1l1ll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1111ll1l111_opy_(bstack1111l11l111_opy_):
    if not bstack1111l11l111_opy_:
        return bstack11l1111_opy_ (u"ࠨࠩᰝ")
    return bstack11l1111_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᰞ").format(bstack1111l11l111_opy_.name, bstack1111l11l111_opy_.email)
def bstack111l11lll1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1l1lll1_opy_ = repo.common_dir
        info = {
            bstack11l1111_opy_ (u"ࠥࡷ࡭ࡧࠢᰟ"): repo.head.commit.hexsha,
            bstack11l1111_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᰠ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l1111_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᰡ"): repo.active_branch.name,
            bstack11l1111_opy_ (u"ࠨࡴࡢࡩࠥᰢ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l1111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᰣ"): bstack1111ll1l111_opy_(repo.head.commit.committer),
            bstack11l1111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᰤ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l1111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᰥ"): bstack1111ll1l111_opy_(repo.head.commit.author),
            bstack11l1111_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᰦ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l1111_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᰧ"): repo.head.commit.message,
            bstack11l1111_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᰨ"): repo.git.rev_parse(bstack11l1111_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᰩ")),
            bstack11l1111_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᰪ"): bstack111l1l1lll1_opy_,
            bstack11l1111_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᰫ"): subprocess.check_output([bstack11l1111_opy_ (u"ࠤࡪ࡭ࡹࠨᰬ"), bstack11l1111_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᰭ"), bstack11l1111_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᰮ")]).strip().decode(
                bstack11l1111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰯ")),
            bstack11l1111_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᰰ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l1111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᰱ"): repo.git.rev_list(
                bstack11l1111_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᰲ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l11llll1_opy_ = []
        for remote in remotes:
            bstack1111llll1l1_opy_ = {
                bstack11l1111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᰳ"): remote.name,
                bstack11l1111_opy_ (u"ࠥࡹࡷࡲࠢᰴ"): remote.url,
            }
            bstack111l11llll1_opy_.append(bstack1111llll1l1_opy_)
        bstack111l1l111ll_opy_ = {
            bstack11l1111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᰵ"): bstack11l1111_opy_ (u"ࠧ࡭ࡩࡵࠤᰶ"),
            **info,
            bstack11l1111_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹ᰷ࠢ"): bstack111l11llll1_opy_
        }
        bstack111l1l111ll_opy_ = bstack111l11111l1_opy_(bstack111l1l111ll_opy_)
        return bstack111l1l111ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l1111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥ᰸").format(err))
        return {}
def bstack11ll1ll1111_opy_(bstack111l11l1l11_opy_=None):
    bstack11l1111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࡧ࡬࡭ࡻࠣࡪࡴࡸ࡭ࡢࡶࡷࡩࡩࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡸࡷࡪࠦࡣࡢࡵࡨࡷࠥ࡬࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧࡱ࡯ࡨࡪࡸࠠࡪࡰࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡪࡴࡲࡤࡦࡴࡶࠤ࠭ࡲࡩࡴࡶ࠯ࠤࡴࡶࡴࡪࡱࡱࡥࡱ࠯࠺ࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡑࡳࡳ࡫࠺ࠡࡏࡲࡲࡴ࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭࠲ࠠࡶࡵࡨࡷࠥࡩࡵࡳࡴࡨࡲࡹࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡞ࡳࡸ࠴ࡧࡦࡶࡦࡻࡩ࠮ࠩ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡈࡱࡵࡺࡹࠡ࡮࡬ࡷࡹ࡛ࠦ࡞࠼ࠣࡑࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡺ࡭ࡹ࡮ࠠ࡯ࡱࠣࡷࡴࡻࡲࡤࡧࡶࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤ࠭ࠢࡵࡩࡹࡻࡲ࡯ࡵࠣ࡟ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡱࡣࡷ࡬ࡸࡀࠠࡎࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡨࠦࡦࡰ࡮ࡧࡩࡷࡹࠠࡵࡱࠣࡥࡳࡧ࡬ࡺࡼࡨࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡩ࡯ࡣࡵࡵ࠯ࠤࡪࡧࡣࡩࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡤࠤ࡫ࡵ࡬ࡥࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ᰹")
    if bstack111l11l1l11_opy_ is None:
        bstack111l11l1l11_opy_ = [os.getcwd()]
    elif isinstance(bstack111l11l1l11_opy_, list) and len(bstack111l11l1l11_opy_) == 0:
        return []
    results = []
    for folder in bstack111l11l1l11_opy_:
        try:
            if not os.path.exists(folder):
                raise Exception(bstack11l1111_opy_ (u"ࠤࡉࡳࡱࡪࡥࡳࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠢ᰺").format(folder))
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l1111_opy_ (u"ࠥࡴࡷࡏࡤࠣ᰻"): bstack11l1111_opy_ (u"ࠦࠧ᰼"),
                bstack11l1111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦ᰽"): [],
                bstack11l1111_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢ᰾"): [],
                bstack11l1111_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢ᰿"): bstack11l1111_opy_ (u"ࠣࠤ᱀"),
                bstack11l1111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡏࡨࡷࡸࡧࡧࡦࡵࠥ᱁"): [],
                bstack11l1111_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦ᱂"): bstack11l1111_opy_ (u"ࠦࠧ᱃"),
                bstack11l1111_opy_ (u"ࠧࡶࡲࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧ᱄"): bstack11l1111_opy_ (u"ࠨࠢ᱅"),
                bstack11l1111_opy_ (u"ࠢࡱࡴࡕࡥࡼࡊࡩࡧࡨࠥ᱆"): bstack11l1111_opy_ (u"ࠣࠤ᱇")
            }
            bstack1111l1ll11l_opy_ = repo.active_branch.name
            bstack1111lll1lll_opy_ = repo.head.commit
            result[bstack11l1111_opy_ (u"ࠤࡳࡶࡎࡪࠢ᱈")] = bstack1111lll1lll_opy_.hexsha
            bstack1111l1l11ll_opy_ = _1111l11l1l1_opy_(repo)
            logger.debug(bstack11l1111_opy_ (u"ࠥࡆࡦࡹࡥࠡࡤࡵࡥࡳࡩࡨࠡࡨࡲࡶࠥࡩ࡯࡮ࡲࡤࡶ࡮ࡹ࡯࡯࠼ࠣࠦ᱉") + str(bstack1111l1l11ll_opy_) + bstack11l1111_opy_ (u"ࠦࠧ᱊"))
            if bstack1111l1l11ll_opy_:
                try:
                    bstack1111l11l11l_opy_ = repo.git.diff(bstack11l1111_opy_ (u"ࠧ࠳࠭࡯ࡣࡰࡩ࠲ࡵ࡮࡭ࡻࠥ᱋"), bstack1lll1ll1111_opy_ (u"ࠨࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂ࠴࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦ᱌")).split(bstack11l1111_opy_ (u"ࠧ࡝ࡰࠪᱍ"))
                    logger.debug(bstack11l1111_opy_ (u"ࠣࡅ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾࠢࡤࡲࡩࠦࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾ࠼ࠣࠦᱎ") + str(bstack1111l11l11l_opy_) + bstack11l1111_opy_ (u"ࠤࠥᱏ"))
                    result[bstack11l1111_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᱐")] = [f.strip() for f in bstack1111l11l11l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll1111_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳ࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽࠣ᱑")))
                except Exception:
                    logger.debug(bstack11l1111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡧ࡮ࡤࡪࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠮ࠡࡈࡤࡰࡱ࡯࡮ࡨࠢࡥࡥࡨࡱࠠࡵࡱࠣࡶࡪࡩࡥ࡯ࡶࠣࡧࡴࡳ࡭ࡪࡶࡶ࠲ࠧ᱒"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l1111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᱓")] = _1111l1l1111_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l1111_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᱔")] = _1111l1l1111_opy_(commits[:5])
            bstack1111l1lll1l_opy_ = set()
            bstack1111l111l11_opy_ = []
            for commit in commits:
                logger.debug(bstack11l1111_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡩ࡯࡮࡯࡬ࡸ࠿ࠦࠢ᱕") + str(commit.message) + bstack11l1111_opy_ (u"ࠤࠥ᱖"))
                bstack1111ll11ll1_opy_ = commit.author.name if commit.author else bstack11l1111_opy_ (u"࡙ࠥࡳࡱ࡮ࡰࡹࡱࠦ᱗")
                bstack1111l1lll1l_opy_.add(bstack1111ll11ll1_opy_)
                bstack1111l111l11_opy_.append({
                    bstack11l1111_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧ᱘"): commit.message.strip(),
                    bstack11l1111_opy_ (u"ࠧࡻࡳࡦࡴࠥ᱙"): bstack1111ll11ll1_opy_
                })
            result[bstack11l1111_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢᱚ")] = list(bstack1111l1lll1l_opy_)
            result[bstack11l1111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᱛ")] = bstack1111l111l11_opy_
            result[bstack11l1111_opy_ (u"ࠣࡲࡵࡈࡦࡺࡥࠣᱜ")] = bstack1111lll1lll_opy_.committed_datetime.strftime(bstack11l1111_opy_ (u"ࠤࠨ࡝࠲ࠫ࡭࠮ࠧࡧࠦᱝ"))
            if (not result[bstack11l1111_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᱞ")] or result[bstack11l1111_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᱟ")].strip() == bstack11l1111_opy_ (u"ࠧࠨᱠ")) and bstack1111lll1lll_opy_.message:
                bstack1111l1ll1ll_opy_ = bstack1111lll1lll_opy_.message.strip().splitlines()
                result[bstack11l1111_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᱡ")] = bstack1111l1ll1ll_opy_[0] if bstack1111l1ll1ll_opy_ else bstack11l1111_opy_ (u"ࠢࠣᱢ")
                if len(bstack1111l1ll1ll_opy_) > 2:
                    result[bstack11l1111_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᱣ")] = bstack11l1111_opy_ (u"ࠩ࡟ࡲࠬᱤ").join(bstack1111l1ll1ll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l1111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࠪࡩࡳࡱࡪࡥࡳ࠼ࠣࡿࢂ࠯࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᱥ").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _111l1111111_opy_(result)
    ]
    return filtered_results
def _111l1111111_opy_(result):
    bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍ࡫࡬ࡱࡧࡵࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡩࡧࠢࡤࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡹࡵ࡭ࡶࠣ࡭ࡸࠦࡶࡢ࡮࡬ࡨࠥ࠮࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠢࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠡࡣࡱࡨࠥࡧࡵࡵࡪࡲࡶࡸ࠯࠮ࠋࠢࠣࠤࠥࠨࠢࠣᱦ")
    return (
        isinstance(result.get(bstack11l1111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᱧ"), None), list)
        and len(result[bstack11l1111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᱨ")]) > 0
        and isinstance(result.get(bstack11l1111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᱩ"), None), list)
        and len(result[bstack11l1111_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᱪ")]) > 0
    )
def _1111l11l1l1_opy_(repo):
    bstack11l1111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡗࡶࡾࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡨࡦࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡩ࡬ࡺࡪࡴࠠࡳࡧࡳࡳࠥࡽࡩࡵࡪࡲࡹࡹࠦࡨࡢࡴࡧࡧࡴࡪࡥࡥࠢࡱࡥࡲ࡫ࡳࠡࡣࡱࡨࠥࡽ࡯ࡳ࡭ࠣࡻ࡮ࡺࡨࠡࡣ࡯ࡰࠥ࡜ࡃࡔࠢࡳࡶࡴࡼࡩࡥࡧࡵࡷ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡥࡶࡦࡴࡣࡩࠢ࡬ࡪࠥࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠬࠡࡧ࡯ࡷࡪࠦࡎࡰࡰࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᱫ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111l111lll_opy_ = origin.refs[bstack11l1111_opy_ (u"ࠪࡌࡊࡇࡄࠨᱬ")]
            target = bstack1111l111lll_opy_.reference.name
            if target.startswith(bstack11l1111_opy_ (u"ࠫࡴࡸࡩࡨ࡫ࡱ࠳ࠬᱭ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l1111_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᱮ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l1l1111_opy_(commits):
    bstack11l1111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡇࡦࡶࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡨ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࡸ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᱯ")
    bstack1111l11l11l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l11l111l_opy_ in diff:
                        if bstack111l11l111l_opy_.a_path:
                            bstack1111l11l11l_opy_.add(bstack111l11l111l_opy_.a_path)
                        if bstack111l11l111l_opy_.b_path:
                            bstack1111l11l11l_opy_.add(bstack111l11l111l_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l11l11l_opy_)
def bstack111l11111l1_opy_(bstack111l1l111ll_opy_):
    bstack111l1111l11_opy_ = bstack1111l111l1l_opy_(bstack111l1l111ll_opy_)
    if bstack111l1111l11_opy_ and bstack111l1111l11_opy_ > bstack11l1l11l1ll_opy_:
        bstack111l1l1llll_opy_ = bstack111l1111l11_opy_ - bstack11l1l11l1ll_opy_
        bstack111l1l1l111_opy_ = bstack1111ll11lll_opy_(bstack111l1l111ll_opy_[bstack11l1111_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᱰ")], bstack111l1l1llll_opy_)
        bstack111l1l111ll_opy_[bstack11l1111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᱱ")] = bstack111l1l1l111_opy_
        logger.info(bstack11l1111_opy_ (u"ࠤࡗ࡬ࡪࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡨࡢࡵࠣࡦࡪ࡫࡮ࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧ࠲࡙ࠥࡩࡻࡧࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࠦࡡࡧࡶࡨࡶࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥࢁࡽࠡࡍࡅࠦᱲ")
                    .format(bstack1111l111l1l_opy_(bstack111l1l111ll_opy_) / 1024))
    return bstack111l1l111ll_opy_
def bstack1111l111l1l_opy_(json_data):
    try:
        if json_data:
            bstack111l1l11lll_opy_ = json.dumps(json_data)
            bstack1111l1l1l11_opy_ = sys.getsizeof(bstack111l1l11lll_opy_)
            return bstack1111l1l1l11_opy_
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠥࡗࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡦࡥࡱࡩࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡌࡖࡓࡓࠦ࡯ࡣ࡬ࡨࡧࡹࡀࠠࡼࡿࠥᱳ").format(e))
    return -1
def bstack1111ll11lll_opy_(field, bstack11111lllll1_opy_):
    try:
        bstack111l111l111_opy_ = len(bytes(bstack11l11l11lll_opy_, bstack11l1111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᱴ")))
        bstack111l1111l1l_opy_ = bytes(field, bstack11l1111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᱵ"))
        bstack1111lllll11_opy_ = len(bstack111l1111l1l_opy_)
        bstack1111l11ll1l_opy_ = ceil(bstack1111lllll11_opy_ - bstack11111lllll1_opy_ - bstack111l111l111_opy_)
        if bstack1111l11ll1l_opy_ > 0:
            bstack1111ll1l1l1_opy_ = bstack111l1111l1l_opy_[:bstack1111l11ll1l_opy_].decode(bstack11l1111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᱶ"), errors=bstack11l1111_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࠧᱷ")) + bstack11l11l11lll_opy_
            return bstack1111ll1l1l1_opy_
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡴࡳࡷࡱࡧࡦࡺࡩ࡯ࡩࠣࡪ࡮࡫࡬ࡥ࠮ࠣࡲࡴࡺࡨࡪࡰࡪࠤࡼࡧࡳࠡࡶࡵࡹࡳࡩࡡࡵࡧࡧࠤ࡭࡫ࡲࡦ࠼ࠣࡿࢂࠨᱸ").format(e))
    return field
def bstack11l11l1lll_opy_():
    env = os.environ
    if (bstack11l1111_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᱹ") in env and len(env[bstack11l1111_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᱺ")]) > 0) or (
            bstack11l1111_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᱻ") in env and len(env[bstack11l1111_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᱼ")]) > 0):
        return {
            bstack11l1111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱽ"): bstack11l1111_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣ᱾"),
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᱿"): env.get(bstack11l1111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᲀ")),
            bstack11l1111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲁ"): env.get(bstack11l1111_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨᲂ")),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲃ"): env.get(bstack11l1111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲄ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠢࡄࡋࠥᲅ")) == bstack11l1111_opy_ (u"ࠣࡶࡵࡹࡪࠨᲆ") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦᲇ"))):
        return {
            bstack11l1111_opy_ (u"ࠥࡲࡦࡳࡥࠣᲈ"): bstack11l1111_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨᲉ"),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲊ"): env.get(bstack11l1111_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᲋")),
            bstack11l1111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᲌"): env.get(bstack11l1111_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧ᲍")),
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᲎"): env.get(bstack11l1111_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨ᲏"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠦࡈࡏࠢᲐ")) == bstack11l1111_opy_ (u"ࠧࡺࡲࡶࡧࠥᲑ") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨᲒ"))):
        return {
            bstack11l1111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲓ"): bstack11l1111_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦᲔ"),
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲕ"): env.get(bstack11l1111_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥᲖ")),
            bstack11l1111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲗ"): env.get(bstack11l1111_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᲘ")),
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲙ"): env.get(bstack11l1111_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲚ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠣࡅࡌࠦᲛ")) == bstack11l1111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲜ") and env.get(bstack11l1111_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦᲝ")) == bstack11l1111_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨᲞ"):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲟ"): bstack11l1111_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣᲠ"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲡ"): None,
            bstack11l1111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲢ"): None,
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲣ"): None
        }
    if env.get(bstack11l1111_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨᲤ")) and env.get(bstack11l1111_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢᲥ")):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲦ"): bstack11l1111_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤᲧ"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲨ"): env.get(bstack11l1111_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨᲩ")),
            bstack11l1111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲪ"): None,
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲫ"): env.get(bstack11l1111_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲬ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠧࡉࡉࠣᲭ")) == bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦᲮ") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨᲯ"))):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨᲰ"): bstack11l1111_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣᲱ"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲲ"): env.get(bstack11l1111_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢᲳ")),
            bstack11l1111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲴ"): None,
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲵ"): env.get(bstack11l1111_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲶ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠣࡅࡌࠦᲷ")) == bstack11l1111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲸ") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨᲹ"))):
        return {
            bstack11l1111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲺ"): bstack11l1111_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣ᲻"),
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲼"): env.get(bstack11l1111_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨᲽ")),
            bstack11l1111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲾ"): env.get(bstack11l1111_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᲿ")),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳀"): env.get(bstack11l1111_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢ᳁"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠧࡉࡉࠣ᳂")) == bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦ᳃") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥ᳄"))):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳅"): bstack11l1111_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤ᳆"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳇"): env.get(bstack11l1111_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣ᳈")),
            bstack11l1111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳉"): env.get(bstack11l1111_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᳊")),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳋"): env.get(bstack11l1111_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦ᳌"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠤࡆࡍࠧ᳍")) == bstack11l1111_opy_ (u"ࠥࡸࡷࡻࡥࠣ᳎") and bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢ᳏"))):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳐"): bstack11l1111_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤ᳑"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳒"): env.get(bstack11l1111_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᳓")),
            bstack11l1111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨ᳔ࠦ"): env.get(bstack11l1111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐ᳕ࠧ")) or env.get(bstack11l1111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋ᳖ࠢ")),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵ᳗ࠦ"): env.get(bstack11l1111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒ᳘ࠣ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤ᳙"))):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳚"): bstack11l1111_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤ᳛"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳜"): bstack11l1111_opy_ (u"ࠦࢀࢃࡻࡾࠤ᳝").format(env.get(bstack11l1111_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨ᳞")), env.get(bstack11l1111_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ᳟࠭"))),
            bstack11l1111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳠"): env.get(bstack11l1111_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢ᳡")),
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲ᳢ࠣ"): env.get(bstack11l1111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆ᳣ࠥ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨ᳤"))):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧ᳥ࠥ"): bstack11l1111_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲ᳦ࠣ"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮᳧ࠥ"): bstack11l1111_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ᳨ࠢ").format(env.get(bstack11l1111_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨᳩ")), env.get(bstack11l1111_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫᳪ")), env.get(bstack11l1111_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬᳫ")), env.get(bstack11l1111_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩᳬ"))),
            bstack11l1111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳭ࠣ"): env.get(bstack11l1111_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᳮ")),
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᳯ"): env.get(bstack11l1111_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᳰ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦᳱ")) and env.get(bstack11l1111_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᳲ")):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᳳ"): bstack11l1111_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣ᳴"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᳵ"): bstack11l1111_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦᳶ").format(env.get(bstack11l1111_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬ᳷")), env.get(bstack11l1111_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨ᳸")), env.get(bstack11l1111_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫ᳹"))),
            bstack11l1111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳺ"): env.get(bstack11l1111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᳻")),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳼"): env.get(bstack11l1111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ᳽"))
        }
    if any([env.get(bstack11l1111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᳾")), env.get(bstack11l1111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤ᳿")), env.get(bstack11l1111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᴀ"))]):
        return {
            bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴁ"): bstack11l1111_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨᴂ"),
            bstack11l1111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴃ"): env.get(bstack11l1111_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᴄ")),
            bstack11l1111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴅ"): env.get(bstack11l1111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᴆ")),
            bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴇ"): env.get(bstack11l1111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴈ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦᴉ")):
        return {
            bstack11l1111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴊ"): bstack11l1111_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣᴋ"),
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴌ"): env.get(bstack11l1111_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰࠧᴍ")),
            bstack11l1111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴎ"): env.get(bstack11l1111_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨࠦᴏ")),
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴐ"): env.get(bstack11l1111_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧᴑ"))
        }
    if env.get(bstack11l1111_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤᴒ")) or env.get(bstack11l1111_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦᴓ")):
        return {
            bstack11l1111_opy_ (u"ࠥࡲࡦࡳࡥࠣᴔ"): bstack11l1111_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶࠧᴕ"),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴖ"): env.get(bstack11l1111_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᴗ")),
            bstack11l1111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴘ"): bstack11l1111_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣᴙ") if env.get(bstack11l1111_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦᴚ")) else None,
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴛ"): env.get(bstack11l1111_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤᴜ"))
        }
    if any([env.get(bstack11l1111_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖࠥᴝ")), env.get(bstack11l1111_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᴞ")), env.get(bstack11l1111_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᴟ"))]):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨᴠ"): bstack11l1111_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤࠣᴡ"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴢ"): None,
            bstack11l1111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴣ"): env.get(bstack11l1111_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤᴤ")),
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴥ"): env.get(bstack11l1111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᴦ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦᴧ")):
        return {
            bstack11l1111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴨ"): bstack11l1111_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨᴩ"),
            bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴪ"): env.get(bstack11l1111_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᴫ")),
            bstack11l1111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴬ"): bstack11l1111_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣᴭ").format(env.get(bstack11l1111_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫᴮ"))) if env.get(bstack11l1111_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠧᴯ")) else None,
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴰ"): env.get(bstack11l1111_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᴱ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨᴲ"))):
        return {
            bstack11l1111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴳ"): bstack11l1111_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹࠣᴴ"),
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴵ"): env.get(bstack11l1111_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨᴶ")),
            bstack11l1111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴷ"): env.get(bstack11l1111_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢᴸ")),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴹ"): env.get(bstack11l1111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᴺ"))
        }
    if bstack1ll11lll11_opy_(env.get(bstack11l1111_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣᴻ"))):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨᴼ"): bstack11l1111_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥᴽ"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴾ"): bstack11l1111_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧᴿ").format(env.get(bstack11l1111_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩᵀ")), env.get(bstack11l1111_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪᵁ")), env.get(bstack11l1111_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧᵂ"))),
            bstack11l1111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵃ"): env.get(bstack11l1111_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦᵄ")),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵅ"): env.get(bstack11l1111_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦᵆ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠧࡉࡉࠣᵇ")) == bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦᵈ") and env.get(bstack11l1111_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢᵉ")) == bstack11l1111_opy_ (u"ࠣ࠳ࠥᵊ"):
        return {
            bstack11l1111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᵋ"): bstack11l1111_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥᵌ"),
            bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᵍ"): bstack11l1111_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣᵎ").format(env.get(bstack11l1111_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪᵏ"))),
            bstack11l1111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵐ"): None,
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵑ"): None,
        }
    if env.get(bstack11l1111_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᵒ")):
        return {
            bstack11l1111_opy_ (u"ࠥࡲࡦࡳࡥࠣᵓ"): bstack11l1111_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨᵔ"),
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵕ"): None,
            bstack11l1111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᵖ"): env.get(bstack11l1111_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣᵗ")),
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵘ"): env.get(bstack11l1111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᵙ"))
        }
    if any([env.get(bstack11l1111_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨᵚ")), env.get(bstack11l1111_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦᵛ")), env.get(bstack11l1111_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥᵜ")), env.get(bstack11l1111_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢᵝ"))]):
        return {
            bstack11l1111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᵞ"): bstack11l1111_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦᵟ"),
            bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᵠ"): None,
            bstack11l1111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᵡ"): env.get(bstack11l1111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᵢ")) or None,
            bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵣ"): env.get(bstack11l1111_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᵤ"), 0)
        }
    if env.get(bstack11l1111_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᵥ")):
        return {
            bstack11l1111_opy_ (u"ࠣࡰࡤࡱࡪࠨᵦ"): bstack11l1111_opy_ (u"ࠤࡊࡳࡈࡊࠢᵧ"),
            bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᵨ"): None,
            bstack11l1111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᵩ"): env.get(bstack11l1111_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᵪ")),
            bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᵫ"): env.get(bstack11l1111_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨᵬ"))
        }
    if env.get(bstack11l1111_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᵭ")):
        return {
            bstack11l1111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᵮ"): bstack11l1111_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨᵯ"),
            bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᵰ"): env.get(bstack11l1111_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᵱ")),
            bstack11l1111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᵲ"): env.get(bstack11l1111_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᵳ")),
            bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵴ"): env.get(bstack11l1111_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᵵ"))
        }
    return {bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵶ"): None}
def get_host_info():
    return {
        bstack11l1111_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨᵷ"): platform.node(),
        bstack11l1111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢᵸ"): platform.system(),
        bstack11l1111_opy_ (u"ࠨࡴࡺࡲࡨࠦᵹ"): platform.machine(),
        bstack11l1111_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣᵺ"): platform.version(),
        bstack11l1111_opy_ (u"ࠣࡣࡵࡧ࡭ࠨᵻ"): platform.architecture()[0]
    }
def bstack1l1l111111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l11l11ll_opy_():
    if bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪᵼ")):
        return bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵽ")
    return bstack11l1111_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪᵾ")
def bstack1111l111ll1_opy_(driver):
    info = {
        bstack11l1111_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᵿ"): driver.capabilities,
        bstack11l1111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪᶀ"): driver.session_id,
        bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨᶁ"): driver.capabilities.get(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᶂ"), None),
        bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫᶃ"): driver.capabilities.get(bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᶄ"), None),
        bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ᶅ"): driver.capabilities.get(bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᶆ"), None),
        bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᶇ"):driver.capabilities.get(bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩᶈ"), None),
    }
    if bstack111l11l11ll_opy_() == bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᶉ"):
        if bstack1111l111ll_opy_():
            info[bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᶊ")] = bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩᶋ")
        elif driver.capabilities.get(bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᶌ"), {}).get(bstack11l1111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᶍ"), False):
            info[bstack11l1111_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᶎ")] = bstack11l1111_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᶏ")
        else:
            info[bstack11l1111_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᶐ")] = bstack11l1111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᶑ")
    return info
def bstack1111l111ll_opy_():
    if bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩᶒ")):
        return True
    if bstack1ll11lll11_opy_(os.environ.get(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬᶓ"), None)):
        return True
    return False
def bstack111ll1l111_opy_(bstack1111lll1l11_opy_, url, data, config):
    headers = config.get(bstack11l1111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᶔ"), None)
    proxies = bstack1111l1l111_opy_(config, url)
    auth = config.get(bstack11l1111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫᶕ"), None)
    response = requests.request(
            bstack1111lll1l11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11l1l1llll_opy_(bstack11l1ll1l1l_opy_, size):
    bstack1ll11111l_opy_ = []
    while len(bstack11l1ll1l1l_opy_) > size:
        bstack1l11lll1l1_opy_ = bstack11l1ll1l1l_opy_[:size]
        bstack1ll11111l_opy_.append(bstack1l11lll1l1_opy_)
        bstack11l1ll1l1l_opy_ = bstack11l1ll1l1l_opy_[size:]
    bstack1ll11111l_opy_.append(bstack11l1ll1l1l_opy_)
    return bstack1ll11111l_opy_
def bstack1111ll1111l_opy_(message, bstack1111l1llll1_opy_=False):
    os.write(1, bytes(message, bstack11l1111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᶖ")))
    os.write(1, bytes(bstack11l1111_opy_ (u"ࠨ࡞ࡱࠫᶗ"), bstack11l1111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᶘ")))
    if bstack1111l1llll1_opy_:
        with open(bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩᶙ") + os.environ[bstack11l1111_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪᶚ")] + bstack11l1111_opy_ (u"ࠬ࠴࡬ࡰࡩࠪᶛ"), bstack11l1111_opy_ (u"࠭ࡡࠨᶜ")) as f:
            f.write(message + bstack11l1111_opy_ (u"ࠧ࡝ࡰࠪᶝ"))
def bstack1lll1lllll1_opy_():
    return os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᶞ")].lower() == bstack11l1111_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᶟ")
def bstack1ll11lll_opy_():
    return bstack1l1l11ll_opy_().replace(tzinfo=None).isoformat() + bstack11l1111_opy_ (u"ࠪ࡞ࠬᶠ")
def bstack1111l1111l1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l1111_opy_ (u"ࠫ࡟࠭ᶡ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l1111_opy_ (u"ࠬࡠࠧᶢ")))).total_seconds() * 1000
def bstack1111ll1l1ll_opy_(timestamp):
    return bstack1111llll111_opy_(timestamp).isoformat() + bstack11l1111_opy_ (u"࡚࠭ࠨᶣ")
def bstack1111lll111l_opy_(bstack111l1l1ll11_opy_):
    date_format = bstack11l1111_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬᶤ")
    bstack1111ll111l1_opy_ = datetime.datetime.strptime(bstack111l1l1ll11_opy_, date_format)
    return bstack1111ll111l1_opy_.isoformat() + bstack11l1111_opy_ (u"ࠨ࡜ࠪᶥ")
def bstack1111lllllll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l1111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶦ")
    else:
        return bstack11l1111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᶧ")
def bstack1ll11lll11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l1111_opy_ (u"ࠫࡹࡸࡵࡦࠩᶨ")
def bstack111l11lllll_opy_(val):
    return val.__str__().lower() == bstack11l1111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᶩ")
def error_handler(bstack111l11ll1ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l11ll1ll_opy_ as e:
                print(bstack11l1111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨᶪ").format(func.__name__, bstack111l11ll1ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l1l11ll1_opy_(bstack1111ll1lll1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111ll1lll1_opy_(cls, *args, **kwargs)
            except bstack111l11ll1ll_opy_ as e:
                print(bstack11l1111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᶫ").format(bstack1111ll1lll1_opy_.__name__, bstack111l11ll1ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l1l11ll1_opy_
    else:
        return decorator
def bstack1l11lllll1_opy_(bstack111ll11l_opy_):
    if os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫᶬ")) is not None:
        return bstack1ll11lll11_opy_(os.getenv(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᶭ")))
    if bstack11l1111_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᶮ") in bstack111ll11l_opy_ and bstack111l11lllll_opy_(bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᶯ")]):
        return False
    if bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᶰ") in bstack111ll11l_opy_ and bstack111l11lllll_opy_(bstack111ll11l_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᶱ")]):
        return False
    return True
def bstack1ll111ll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111l11111l_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢᶲ"), None)
        return bstack1111l11111l_opy_ is None or bstack1111l11111l_opy_ == bstack11l1111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᶳ")
    except Exception as e:
        return False
def bstack1l11111111_opy_(hub_url, CONFIG):
    if bstack11l1l1l111_opy_() <= version.parse(bstack11l1111_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᶴ")):
        if hub_url:
            return bstack11l1111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᶵ") + hub_url + bstack11l1111_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᶶ")
        return bstack1ll11l1lll_opy_
    if hub_url:
        return bstack11l1111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᶷ") + hub_url + bstack11l1111_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᶸ")
    return bstack1l111l111_opy_
def bstack111l11lll11_opy_():
    return isinstance(os.getenv(bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭ᶹ")), str)
def bstack11ll11lll_opy_(url):
    return urlparse(url).hostname
def bstack11ll1ll11_opy_(hostname):
    for bstack1l111l1ll_opy_ in bstack1lllllll1l_opy_:
        regex = re.compile(bstack1l111l1ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l1llll1ll_opy_(bstack111l11l11l1_opy_, file_name, logger):
    bstack1111llll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠨࢀࠪᶺ")), bstack111l11l11l1_opy_)
    try:
        if not os.path.exists(bstack1111llll1l_opy_):
            os.makedirs(bstack1111llll1l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠩࢁࠫᶻ")), bstack111l11l11l1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l1111_opy_ (u"ࠪࡻࠬᶼ")):
                pass
            with open(file_path, bstack11l1111_opy_ (u"ࠦࡼ࠱ࠢᶽ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11ll1ll1l1_opy_.format(str(e)))
def bstack11l1lllll11_opy_(file_name, key, value, logger):
    file_path = bstack11l1llll1ll_opy_(bstack11l1111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᶾ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111lll1l1l_opy_ = json.load(open(file_path, bstack11l1111_opy_ (u"࠭ࡲࡣࠩᶿ")))
        else:
            bstack111lll1l1l_opy_ = {}
        bstack111lll1l1l_opy_[key] = value
        with open(file_path, bstack11l1111_opy_ (u"ࠢࡸ࠭ࠥ᷀")) as outfile:
            json.dump(bstack111lll1l1l_opy_, outfile)
def bstack11l11ll11l_opy_(file_name, logger):
    file_path = bstack11l1llll1ll_opy_(bstack11l1111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᷁"), file_name, logger)
    bstack111lll1l1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l1111_opy_ (u"ࠩࡵ᷂ࠫ")) as bstack1ll111l1ll_opy_:
            bstack111lll1l1l_opy_ = json.load(bstack1ll111l1ll_opy_)
    return bstack111lll1l1l_opy_
def bstack11lll1l1l1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩ࠿ࠦࠧ᷃") + file_path + bstack11l1111_opy_ (u"ࠫࠥ࠭᷄") + str(e))
def bstack11l1l1l111_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l1111_opy_ (u"ࠧࡂࡎࡐࡖࡖࡉ࡙ࡄࠢ᷅")
def bstack11ll11l1ll_opy_(config):
    if bstack11l1111_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬ᷆") in config:
        del (config[bstack11l1111_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭᷇")])
        return False
    if bstack11l1l1l111_opy_() < version.parse(bstack11l1111_opy_ (u"ࠨ࠵࠱࠸࠳࠶ࠧ᷈")):
        return False
    if bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠩ࠷࠲࠶࠴࠵ࠨ᷉")):
        return True
    if bstack11l1111_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅ᷊ࠪ") in config and config[bstack11l1111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ᷋")] is False:
        return False
    else:
        return True
def bstack1ll1111l1_opy_(args_list, bstack1111ll111ll_opy_):
    index = -1
    for value in bstack1111ll111ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l11l1lll_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l11l1lll_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1ll1l1ll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1ll1l1ll_opy_ = bstack1ll1l1ll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l1111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᷌"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l1111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᷍"), exception=exception)
    def bstack11111111ll_opy_(self):
        if self.result != bstack11l1111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ᷎ࠧ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l1111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱ᷏ࠦ") in self.exception_type:
            return bstack11l1111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴ᷐ࠥ")
        return bstack11l1111_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦ᷑")
    def bstack111l1111ll1_opy_(self):
        if self.result != bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᷒"):
            return None
        if self.bstack1ll1l1ll_opy_:
            return self.bstack1ll1l1ll_opy_
        return bstack111l111llll_opy_(self.exception)
def bstack111l111llll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l11llll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1llll11l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l1111l11_opy_(config, logger):
    try:
        import playwright
        bstack111l111l1l1_opy_ = playwright.__file__
        bstack1111l1ll111_opy_ = os.path.split(bstack111l111l1l1_opy_)
        bstack1111ll1ll11_opy_ = bstack1111l1ll111_opy_[0] + bstack11l1111_opy_ (u"ࠬ࠵ࡤࡳ࡫ࡹࡩࡷ࠵ࡰࡢࡥ࡮ࡥ࡬࡫࠯࡭࡫ࡥ࠳ࡨࡲࡩ࠰ࡥ࡯࡭࠳ࡰࡳࠨᷓ")
        os.environ[bstack11l1111_opy_ (u"࠭ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠩᷔ")] = bstack111lll1ll_opy_(config)
        with open(bstack1111ll1ll11_opy_, bstack11l1111_opy_ (u"ࠧࡳࠩᷕ")) as f:
            file_content = f.read()
            bstack1111l111111_opy_ = bstack11l1111_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧᷖ")
            bstack1111lll11l1_opy_ = file_content.find(bstack1111l111111_opy_)
            if bstack1111lll11l1_opy_ == -1:
              process = subprocess.Popen(bstack11l1111_opy_ (u"ࠤࡱࡴࡲࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹࠨᷗ"), shell=True, cwd=bstack1111l1ll111_opy_[0])
              process.wait()
              bstack111l111ll11_opy_ = bstack11l1111_opy_ (u"ࠪࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴࠣ࠽ࠪᷘ")
              bstack1111l11l1ll_opy_ = bstack11l1111_opy_ (u"ࠦࠧࠨࠠ࡝ࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࡢࠢ࠼ࠢࡦࡳࡳࡹࡴࠡࡽࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵࠦࡽࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫ࠮ࡁࠠࡪࡨࠣࠬࡵࡸ࡯ࡤࡧࡶࡷ࠳࡫࡮ࡷ࠰ࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝࠮ࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠪࠬ࠿ࠥࠨࠢࠣᷙ")
              bstack111l111l11l_opy_ = file_content.replace(bstack111l111ll11_opy_, bstack1111l11l1ll_opy_)
              with open(bstack1111ll1ll11_opy_, bstack11l1111_opy_ (u"ࠬࡽࠧᷚ")) as f:
                f.write(bstack111l111l11l_opy_)
    except Exception as e:
        logger.error(bstack1l11ll1l1_opy_.format(str(e)))
def bstack11l11l111l_opy_():
  try:
    bstack11111llll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ᷛ"))
    bstack111l1l1l1l1_opy_ = []
    if os.path.exists(bstack11111llll1l_opy_):
      with open(bstack11111llll1l_opy_) as f:
        bstack111l1l1l1l1_opy_ = json.load(f)
      os.remove(bstack11111llll1l_opy_)
    return bstack111l1l1l1l1_opy_
  except:
    pass
  return []
def bstack1l111111l_opy_(bstack11111ll111_opy_):
  try:
    bstack111l1l1l1l1_opy_ = []
    bstack11111llll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᷜ"))
    if os.path.exists(bstack11111llll1l_opy_):
      with open(bstack11111llll1l_opy_) as f:
        bstack111l1l1l1l1_opy_ = json.load(f)
    bstack111l1l1l1l1_opy_.append(bstack11111ll111_opy_)
    with open(bstack11111llll1l_opy_, bstack11l1111_opy_ (u"ࠨࡹࠪᷝ")) as f:
        json.dump(bstack111l1l1l1l1_opy_, f)
  except:
    pass
def bstack1lll11l1ll_opy_(logger, bstack111l11ll111_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l1111_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᷞ"), bstack11l1111_opy_ (u"ࠪࠫᷟ"))
    if test_name == bstack11l1111_opy_ (u"ࠫࠬᷠ"):
        test_name = threading.current_thread().__dict__.get(bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡇࡪࡤࡠࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠫᷡ"), bstack11l1111_opy_ (u"࠭ࠧᷢ"))
    bstack111l11ll11l_opy_ = bstack11l1111_opy_ (u"ࠧ࠭ࠢࠪᷣ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l11ll111_opy_:
        bstack11lll1111_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᷤ"), bstack11l1111_opy_ (u"ࠩ࠳ࠫᷥ"))
        bstack11l111lll1_opy_ = {bstack11l1111_opy_ (u"ࠪࡲࡦࡳࡥࠨᷦ"): test_name, bstack11l1111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷧ"): bstack111l11ll11l_opy_, bstack11l1111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷨ"): bstack11lll1111_opy_}
        bstack1111l1l1lll_opy_ = []
        bstack111l111l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᷩ"))
        if os.path.exists(bstack111l111l1ll_opy_):
            with open(bstack111l111l1ll_opy_) as f:
                bstack1111l1l1lll_opy_ = json.load(f)
        bstack1111l1l1lll_opy_.append(bstack11l111lll1_opy_)
        with open(bstack111l111l1ll_opy_, bstack11l1111_opy_ (u"ࠧࡸࠩᷪ")) as f:
            json.dump(bstack1111l1l1lll_opy_, f)
    else:
        bstack11l111lll1_opy_ = {bstack11l1111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᷫ"): test_name, bstack11l1111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᷬ"): bstack111l11ll11l_opy_, bstack11l1111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᷭ"): str(multiprocessing.current_process().name)}
        if bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨᷮ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11l111lll1_opy_)
  except Exception as e:
      logger.warn(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡱࡻࡷࡩࡸࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᷯ").format(e))
def bstack111l1l1l1_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩᷰ"))
    try:
      bstack1111lll11ll_opy_ = []
      bstack11l111lll1_opy_ = {bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᷱ"): test_name, bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᷲ"): error_message, bstack11l1111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᷳ"): index}
      bstack1111ll11l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᷴ"))
      if os.path.exists(bstack1111ll11l11_opy_):
          with open(bstack1111ll11l11_opy_) as f:
              bstack1111lll11ll_opy_ = json.load(f)
      bstack1111lll11ll_opy_.append(bstack11l111lll1_opy_)
      with open(bstack1111ll11l11_opy_, bstack11l1111_opy_ (u"ࠫࡼ࠭᷵")) as f:
          json.dump(bstack1111lll11ll_opy_, f)
    except Exception as e:
      logger.warn(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡳࡱࡥࡳࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣ᷶").format(e))
    return
  bstack1111lll11ll_opy_ = []
  bstack11l111lll1_opy_ = {bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨ᷷ࠫ"): test_name, bstack11l1111_opy_ (u"ࠧࡦࡴࡵࡳࡷ᷸࠭"): error_message, bstack11l1111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾ᷹ࠧ"): index}
  bstack1111ll11l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰ᷺ࠪ"))
  lock_file = bstack1111ll11l11_opy_ + bstack11l1111_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩ᷻")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111ll11l11_opy_):
          with open(bstack1111ll11l11_opy_, bstack11l1111_opy_ (u"ࠫࡷ࠭᷼")) as f:
              content = f.read().strip()
              if content:
                  bstack1111lll11ll_opy_ = json.load(open(bstack1111ll11l11_opy_))
      bstack1111lll11ll_opy_.append(bstack11l111lll1_opy_)
      with open(bstack1111ll11l11_opy_, bstack11l1111_opy_ (u"ࠬࡽ᷽ࠧ")) as f:
          json.dump(bstack1111lll11ll_opy_, f)
  except Exception as e:
    logger.warn(bstack11l1111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨ࠼ࠣࡿࢂࠨ᷾").format(e))
def bstack11llll1l1_opy_(bstack1ll1l1llll_opy_, name, logger):
  try:
    bstack11l111lll1_opy_ = {bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩ᷿ࠬ"): name, bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧḀ"): bstack1ll1l1llll_opy_, bstack11l1111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨḁ"): str(threading.current_thread()._name)}
    return bstack11l111lll1_opy_
  except Exception as e:
    logger.warn(bstack11l1111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡨࡥࡩࡣࡹࡩࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢḂ").format(e))
  return
def bstack1111l1l111l_opy_():
    return platform.system() == bstack11l1111_opy_ (u"ࠫ࡜࡯࡮ࡥࡱࡺࡷࠬḃ")
def bstack1ll1111111_opy_(bstack1111ll11111_opy_, config, logger):
    bstack1111lll1l1l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111ll11111_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡰࡹ࡫ࡲࠡࡥࡲࡲ࡫࡯ࡧࠡ࡭ࡨࡽࡸࠦࡢࡺࠢࡵࡩ࡬࡫ࡸࠡ࡯ࡤࡸࡨ࡮࠺ࠡࡽࢀࠦḄ").format(e))
    return bstack1111lll1l1l_opy_
def bstack11l1l1l111l_opy_(bstack111l1l1l11l_opy_, bstack1111ll1llll_opy_):
    bstack1111l11ll11_opy_ = version.parse(bstack111l1l1l11l_opy_)
    bstack1111l1111ll_opy_ = version.parse(bstack1111ll1llll_opy_)
    if bstack1111l11ll11_opy_ > bstack1111l1111ll_opy_:
        return 1
    elif bstack1111l11ll11_opy_ < bstack1111l1111ll_opy_:
        return -1
    else:
        return 0
def bstack1l1l11ll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111llll111_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l1l1l1l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1lll1lllll_opy_(options, framework, config, bstack111l1lll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l1111_opy_ (u"࠭ࡧࡦࡶࠪḅ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l11lll1ll_opy_ = caps.get(bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨḆ"))
    bstack1111lllll1l_opy_ = True
    bstack1ll1l1ll1l_opy_ = os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ḇ")]
    bstack1l111l1111l_opy_ = config.get(bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḈ"), False)
    if bstack1l111l1111l_opy_:
        bstack1l11ll1l11l_opy_ = config.get(bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḉ"), {})
        bstack1l11ll1l11l_opy_[bstack11l1111_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧḊ")] = os.getenv(bstack11l1111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪḋ"))
        bstack1111ll1ll1l_opy_ = json.loads(os.getenv(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧḌ"), bstack11l1111_opy_ (u"ࠧࡼࡿࠪḍ"))).get(bstack11l1111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩḎ"))
    if bstack111l11lllll_opy_(caps.get(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡷࡶࡩ࡜࠹ࡃࠨḏ"))) or bstack111l11lllll_opy_(caps.get(bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡥࡷ࠴ࡥࠪḐ"))):
        bstack1111lllll1l_opy_ = False
    if bstack11ll11l1ll_opy_({bstack11l1111_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦḑ"): bstack1111lllll1l_opy_}):
        bstack1l11lll1ll_opy_ = bstack1l11lll1ll_opy_ or {}
        bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḒ")] = bstack1111l1l1l1l_opy_(framework)
        bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḓ")] = bstack1lll1lllll1_opy_()
        bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḔ")] = bstack1ll1l1ll1l_opy_
        bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḕ")] = bstack111l1lll1_opy_
        if bstack1l111l1111l_opy_:
            bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḖ")] = bstack1l111l1111l_opy_
            bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḗ")] = bstack1l11ll1l11l_opy_
            bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḘ")][bstack11l1111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ḙ")] = bstack1111ll1ll1l_opy_
        if getattr(options, bstack11l1111_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧḚ"), None):
            options.set_capability(bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨḛ"), bstack1l11lll1ll_opy_)
        else:
            options[bstack11l1111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩḜ")] = bstack1l11lll1ll_opy_
    else:
        if getattr(options, bstack11l1111_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪḝ"), None):
            options.set_capability(bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫḞ"), bstack1111l1l1l1l_opy_(framework))
            options.set_capability(bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬḟ"), bstack1lll1lllll1_opy_())
            options.set_capability(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧḠ"), bstack1ll1l1ll1l_opy_)
            options.set_capability(bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧḡ"), bstack111l1lll1_opy_)
            if bstack1l111l1111l_opy_:
                options.set_capability(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭Ḣ"), bstack1l111l1111l_opy_)
                options.set_capability(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧḣ"), bstack1l11ll1l11l_opy_)
                options.set_capability(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳ࠯ࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩḤ"), bstack1111ll1ll1l_opy_)
        else:
            options[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫḥ")] = bstack1111l1l1l1l_opy_(framework)
            options[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬḦ")] = bstack1lll1lllll1_opy_()
            options[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧḧ")] = bstack1ll1l1ll1l_opy_
            options[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧḨ")] = bstack111l1lll1_opy_
            if bstack1l111l1111l_opy_:
                options[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ḩ")] = bstack1l111l1111l_opy_
                options[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧḪ")] = bstack1l11ll1l11l_opy_
                options[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨḫ")][bstack11l1111_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫḬ")] = bstack1111ll1ll1l_opy_
    return options
def bstack1111l1lllll_opy_(ws_endpoint, framework):
    bstack111l1lll1_opy_ = bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨḭ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l1111_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫḮ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l1111_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬḯ"))[0]
        if bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪḰ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l11l1ll1_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l1111_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḱ"))[1]))
            bstack111l11l1ll1_opy_ = bstack111l11l1ll1_opy_ or {}
            bstack1ll1l1ll1l_opy_ = os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧḲ")]
            bstack111l11l1ll1_opy_[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫḳ")] = str(framework) + str(__version__)
            bstack111l11l1ll1_opy_[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬḴ")] = bstack1lll1lllll1_opy_()
            bstack111l11l1ll1_opy_[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧḵ")] = bstack1ll1l1ll1l_opy_
            bstack111l11l1ll1_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧḶ")] = bstack111l1lll1_opy_
            ws_endpoint = ws_endpoint.split(bstack11l1111_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ḷ"))[0] + bstack11l1111_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḸ") + urllib.parse.quote(json.dumps(bstack111l11l1ll1_opy_))
    return ws_endpoint
def bstack1l1ll1ll1l_opy_():
    global bstack1l11l11l11_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l11l11l11_opy_ = BrowserType.connect
    return bstack1l11l11l11_opy_
def bstack111l1l1lll_opy_(framework_name):
    global bstack1l11l1l1l1_opy_
    bstack1l11l1l1l1_opy_ = framework_name
    return framework_name
def bstack1111l11lll_opy_(self, *args, **kwargs):
    global bstack1l11l11l11_opy_
    try:
        global bstack1l11l1l1l1_opy_
        if bstack11l1111_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭ḹ") in kwargs:
            kwargs[bstack11l1111_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḺ")] = bstack1111l1lllll_opy_(
                kwargs.get(bstack11l1111_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨḻ"), None),
                bstack1l11l1l1l1_opy_
            )
    except Exception as e:
        logger.error(bstack11l1111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧḼ").format(str(e)))
    return bstack1l11l11l11_opy_(self, *args, **kwargs)
def bstack1111l11lll1_opy_(bstack111l1ll1111_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1111l1l111_opy_(bstack111l1ll1111_opy_, bstack11l1111_opy_ (u"ࠨࠢḽ"))
        if proxies and proxies.get(bstack11l1111_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨḾ")):
            parsed_url = urlparse(proxies.get(bstack11l1111_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢḿ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬṀ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l1111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ṁ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧṂ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l1111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨṃ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1l111lll_opy_(bstack111l1ll1111_opy_):
    bstack111l1111lll_opy_ = {
        bstack11l11ll1l1l_opy_[bstack111l11111ll_opy_]: bstack111l1ll1111_opy_[bstack111l11111ll_opy_]
        for bstack111l11111ll_opy_ in bstack111l1ll1111_opy_
        if bstack111l11111ll_opy_ in bstack11l11ll1l1l_opy_
    }
    bstack111l1111lll_opy_[bstack11l1111_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨṄ")] = bstack1111l11lll1_opy_(bstack111l1ll1111_opy_, bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢṅ")))
    bstack1111llll1ll_opy_ = [element.lower() for element in bstack11l11l1lll1_opy_]
    bstack1111l1l11l1_opy_(bstack111l1111lll_opy_, bstack1111llll1ll_opy_)
    return bstack111l1111lll_opy_
def bstack1111l1l11l1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l1111_opy_ (u"ࠣࠬ࠭࠮࠯ࠨṆ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l1l11l1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l1l11l1_opy_(item, keys)
def bstack1ll1l11llll_opy_():
    bstack111l111ll1l_opy_ = [os.environ.get(bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡌࡐࡊ࡙࡟ࡅࡋࡕࠦṇ")), os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠥࢂࠧṈ")), bstack11l1111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫṉ")), os.path.join(bstack11l1111_opy_ (u"ࠬ࠵ࡴ࡮ࡲࠪṊ"), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ṋ"))]
    for path in bstack111l111ll1l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l1111_opy_ (u"ࠢࡇ࡫࡯ࡩࠥ࠭ࠢṌ") + str(path) + bstack11l1111_opy_ (u"ࠣࠩࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠦṍ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l1111_opy_ (u"ࠤࡊ࡭ࡻ࡯࡮ࡨࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࡹࠠࡧࡱࡵࠤࠬࠨṎ") + str(path) + bstack11l1111_opy_ (u"ࠥࠫࠧṏ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l1111_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦṐ") + str(path) + bstack11l1111_opy_ (u"ࠧ࠭ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡪࡤࡷࠥࡺࡨࡦࠢࡵࡩࡶࡻࡩࡳࡧࡧࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴ࠰ࠥṑ"))
            else:
                logger.debug(bstack11l1111_opy_ (u"ࠨࡃࡳࡧࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࠧࠣṒ") + str(path) + bstack11l1111_opy_ (u"ࠢࠨࠢࡺ࡭ࡹ࡮ࠠࡸࡴ࡬ࡸࡪࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰ࠱ࠦṓ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l1111_opy_ (u"ࠣࡑࡳࡩࡷࡧࡴࡪࡱࡱࠤࡸࡻࡣࡤࡧࡨࡨࡪࡪࠠࡧࡱࡵࠤࠬࠨṔ") + str(path) + bstack11l1111_opy_ (u"ࠤࠪ࠲ࠧṕ"))
            return path
        except Exception as e:
            logger.debug(bstack11l1111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡹࡵࠦࡦࡪ࡮ࡨࠤࠬࢁࡰࡢࡶ࡫ࢁࠬࡀࠠࠣṖ") + str(e) + bstack11l1111_opy_ (u"ࠦࠧṗ"))
    logger.debug(bstack11l1111_opy_ (u"ࠧࡇ࡬࡭ࠢࡳࡥࡹ࡮ࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠤṘ"))
    return None
@measure(event_name=EVENTS.bstack11l11lll1ll_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack1l1l1l11l11_opy_(binary_path, bstack1l11ll1lll1_opy_, bs_config):
    logger.debug(bstack11l1111_opy_ (u"ࠨࡃࡶࡴࡵࡩࡳࡺࠠࡄࡎࡌࠤࡕࡧࡴࡩࠢࡩࡳࡺࡴࡤ࠻ࠢࡾࢁࠧṙ").format(binary_path))
    bstack111l11l1111_opy_ = bstack11l1111_opy_ (u"ࠧࠨṚ")
    bstack111l1l11l11_opy_ = {
        bstack11l1111_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ṛ"): __version__,
        bstack11l1111_opy_ (u"ࠤࡲࡷࠧṜ"): platform.system(),
        bstack11l1111_opy_ (u"ࠥࡳࡸࡥࡡࡳࡥ࡫ࠦṝ"): platform.machine(),
        bstack11l1111_opy_ (u"ࠦࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠤṞ"): bstack11l1111_opy_ (u"ࠬ࠶ࠧṟ"),
        bstack11l1111_opy_ (u"ࠨࡳࡥ࡭ࡢࡰࡦࡴࡧࡶࡣࡪࡩࠧṠ"): bstack11l1111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧṡ")
    }
    bstack1111ll11l1l_opy_(bstack111l1l11l11_opy_)
    try:
        if binary_path:
            if bstack1111l1l111l_opy_():
                bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"ࠨࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭Ṣ")] = subprocess.check_output([binary_path, bstack11l1111_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥṣ")]).strip().decode(bstack11l1111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩṤ"))
            else:
                bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩṥ")] = subprocess.check_output([binary_path, bstack11l1111_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨṦ")], stderr=subprocess.DEVNULL).strip().decode(bstack11l1111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬṧ"))
        response = requests.request(
            bstack11l1111_opy_ (u"ࠧࡈࡇࡗࠫṨ"),
            url=bstack1llll11l11_opy_(bstack11l11llllll_opy_),
            headers=None,
            auth=(bs_config[bstack11l1111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪṩ")], bs_config[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬṪ")]),
            json=None,
            params=bstack111l1l11l11_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l1111_opy_ (u"ࠪࡹࡷࡲࠧṫ") in data.keys() and bstack11l1111_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨࡤࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪṬ") in data.keys():
            logger.debug(bstack11l1111_opy_ (u"ࠧࡔࡥࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡢࡪࡰࡤࡶࡾ࠲ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯࠼ࠣࡿࢂࠨṭ").format(bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫṮ")]))
            if bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪṯ") in os.environ:
                logger.debug(bstack11l1111_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡧࡳࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠤ࡮ࡹࠠࡴࡧࡷࠦṰ"))
                data[bstack11l1111_opy_ (u"ࠩࡸࡶࡱ࠭ṱ")] = os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭Ṳ")]
            bstack1111llllll1_opy_ = bstack1111l1lll11_opy_(data[bstack11l1111_opy_ (u"ࠫࡺࡸ࡬ࠨṳ")], bstack1l11ll1lll1_opy_)
            bstack111l11l1111_opy_ = os.path.join(bstack1l11ll1lll1_opy_, bstack1111llllll1_opy_)
            os.chmod(bstack111l11l1111_opy_, 0o777) # bstack111l111111l_opy_ permission
            return bstack111l11l1111_opy_
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡰࡨࡻ࡙ࠥࡄࡌࠢࡾࢁࠧṴ").format(e))
    return binary_path
def bstack1111ll11l1l_opy_(bstack111l1l11l11_opy_):
    try:
        if bstack11l1111_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬṵ") not in bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"ࠧࡰࡵࠪṶ")].lower():
            return
        if os.path.exists(bstack11l1111_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥṷ")):
            with open(bstack11l1111_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṸ"), bstack11l1111_opy_ (u"ࠥࡶࠧṹ")) as f:
                bstack1111lll1ll1_opy_ = {}
                for line in f:
                    if bstack11l1111_opy_ (u"ࠦࡂࠨṺ") in line:
                        key, value = line.rstrip().split(bstack11l1111_opy_ (u"ࠧࡃࠢṻ"), 1)
                        bstack1111lll1ll1_opy_[key] = value.strip(bstack11l1111_opy_ (u"࠭ࠢ࡝ࠩࠪṼ"))
                bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṽ")] = bstack1111lll1ll1_opy_.get(bstack11l1111_opy_ (u"ࠣࡋࡇࠦṾ"), bstack11l1111_opy_ (u"ࠤࠥṿ"))
        elif os.path.exists(bstack11l1111_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡣ࡯ࡴ࡮ࡴࡥ࠮ࡴࡨࡰࡪࡧࡳࡦࠤẀ")):
            bstack111l1l11l11_opy_[bstack11l1111_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫẁ")] = bstack11l1111_opy_ (u"ࠬࡧ࡬ࡱ࡫ࡱࡩࠬẂ")
    except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡤࡪࡵࡷࡶࡴࠦ࡯ࡧࠢ࡯࡭ࡳࡻࡸࠣẃ") + e)
@measure(event_name=EVENTS.bstack11l11l1l111_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack1111l1lll11_opy_(bstack1111llll11l_opy_, bstack111l1l1ll1l_opy_):
    logger.debug(bstack11l1111_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳ࠺ࠡࠤẄ") + str(bstack1111llll11l_opy_) + bstack11l1111_opy_ (u"ࠣࠤẅ"))
    zip_path = os.path.join(bstack111l1l1ll1l_opy_, bstack11l1111_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࡥࡦࡪ࡮ࡨ࠲ࡿ࡯ࡰࠣẆ"))
    bstack1111llllll1_opy_ = bstack11l1111_opy_ (u"ࠪࠫẇ")
    with requests.get(bstack1111llll11l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l1111_opy_ (u"ࠦࡼࡨࠢẈ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l1111_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾ࠴ࠢẉ"))
    with zipfile.ZipFile(zip_path, bstack11l1111_opy_ (u"࠭ࡲࠨẊ")) as zip_ref:
        bstack111l1l111l1_opy_ = zip_ref.namelist()
        if len(bstack111l1l111l1_opy_) > 0:
            bstack1111llllll1_opy_ = bstack111l1l111l1_opy_[0] # bstack111l11ll1l1_opy_ bstack11l11l1111l_opy_ will be bstack1111l1ll1l1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l1l1ll1l_opy_)
        logger.debug(bstack11l1111_opy_ (u"ࠢࡇ࡫࡯ࡩࡸࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥ࡫ࡸࡵࡴࡤࡧࡹ࡫ࡤࠡࡶࡲࠤࠬࠨẋ") + str(bstack111l1l1ll1l_opy_) + bstack11l1111_opy_ (u"ࠣࠩࠥẌ"))
    os.remove(zip_path)
    return bstack1111llllll1_opy_
def get_cli_dir():
    bstack111l1l11111_opy_ = bstack1ll1l11llll_opy_()
    if bstack111l1l11111_opy_:
        bstack1l11ll1lll1_opy_ = os.path.join(bstack111l1l11111_opy_, bstack11l1111_opy_ (u"ࠤࡦࡰ࡮ࠨẍ"))
        if not os.path.exists(bstack1l11ll1lll1_opy_):
            os.makedirs(bstack1l11ll1lll1_opy_, mode=0o777, exist_ok=True)
        return bstack1l11ll1lll1_opy_
    else:
        raise FileNotFoundError(bstack11l1111_opy_ (u"ࠥࡒࡴࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽ࠳ࠨẎ"))
def bstack1l1l1ll1l1l_opy_(bstack1l11ll1lll1_opy_):
    bstack11l1111_opy_ (u"ࠦࠧࠨࡇࡦࡶࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡲࠥࡧࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠨࠢࠣẏ")
    bstack111l111lll1_opy_ = [
        os.path.join(bstack1l11ll1lll1_opy_, f)
        for f in os.listdir(bstack1l11ll1lll1_opy_)
        if os.path.isfile(os.path.join(bstack1l11ll1lll1_opy_, f)) and f.startswith(bstack11l1111_opy_ (u"ࠧࡨࡩ࡯ࡣࡵࡽ࠲ࠨẐ"))
    ]
    if len(bstack111l111lll1_opy_) > 0:
        return max(bstack111l111lll1_opy_, key=os.path.getmtime) # get bstack111l1l11l1l_opy_ binary
    return bstack11l1111_opy_ (u"ࠨࠢẑ")
def bstack111l11l1l1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111l11ll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111l11ll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11llll111_opy_(data, keys, default=None):
    bstack11l1111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡔࡣࡩࡩࡱࡿࠠࡨࡧࡷࠤࡦࠦ࡮ࡦࡵࡷࡩࡩࠦࡶࡢ࡮ࡸࡩࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡤࡸࡦࡀࠠࡕࡪࡨࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵࠢࡷࡳࠥࡺࡲࡢࡸࡨࡶࡸ࡫࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡱࡥࡺࡵ࠽ࠤࡆࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠ࡬ࡧࡼࡷ࠴࡯࡮ࡥ࡫ࡦࡩࡸࠦࡲࡦࡲࡵࡩࡸ࡫࡮ࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡥࡧࡣࡸࡰࡹࡀࠠࡗࡣ࡯ࡹࡪࠦࡴࡰࠢࡵࡩࡹࡻࡲ࡯ࠢ࡬ࡪࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦ࠺ࡳࡧࡷࡹࡷࡴ࠺ࠡࡖ࡫ࡩࠥࡼࡡ࡭ࡷࡨࠤࡦࡺࠠࡵࡪࡨࠤࡳ࡫ࡳࡵࡧࡧࠤࡵࡧࡴࡩ࠮ࠣࡳࡷࠦࡤࡦࡨࡤࡹࡱࡺࠠࡪࡨࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠴ࠊࠡࠢࠣࠤࠧࠨࠢẒ")
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