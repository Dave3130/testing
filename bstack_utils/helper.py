# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
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
from bstack_utils.constants import (bstack11l11ll111_opy_, bstack111l11ll11_opy_, bstack111l1111l_opy_,
                                    bstack11l11l11l11_opy_, bstack11l1l111lll_opy_, bstack11l11l11ll1_opy_, bstack11l11l1l1l1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111l111ll1_opy_, bstack1l111l11ll_opy_
from bstack_utils.proxy import bstack111l11l1l1_opy_, bstack1lll11l11l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111111l11l_opy_
from bstack_utils.bstack1l1l1ll11_opy_ import bstack1ll11llll_opy_
from browserstack_sdk._version import __version__
bstack111lll11_opy_ = Config.bstack1111llll_opy_()
logger = bstack111111l11l_opy_.get_logger(__name__, bstack111111l11l_opy_.bstack1l1l11l111l_opy_())
def bstack111l1l1111l_opy_(config):
    return config[bstack11111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᰛ")]
def bstack11111llllll_opy_(config):
    return config[bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᰜ")]
def bstack1lll1111l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l11ll11l_opy_(obj):
    values = []
    bstack1111ll1l11l_opy_ = re.compile(bstack11111_opy_ (u"ࡳࠤࡡࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࡝ࡦ࠮ࠨࠧᰝ"), re.I)
    for key in obj.keys():
        if bstack1111ll1l11l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111l1ll11l_opy_(config):
    tags = []
    tags.extend(bstack111l11ll11l_opy_(os.environ))
    tags.extend(bstack111l11ll11l_opy_(config))
    return tags
def bstack111l1l1ll1l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l11l1ll1_opy_(bstack111l1111111_opy_):
    if not bstack111l1111111_opy_:
        return bstack11111_opy_ (u"ࠩࠪᰞ")
    return bstack11111_opy_ (u"ࠥࡿࢂࠦࠨࡼࡿࠬࠦᰟ").format(bstack111l1111111_opy_.name, bstack111l1111111_opy_.email)
def bstack1111l11l1ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l11lll11_opy_ = repo.common_dir
        info = {
            bstack11111_opy_ (u"ࠦࡸ࡮ࡡࠣᰠ"): repo.head.commit.hexsha,
            bstack11111_opy_ (u"ࠧࡹࡨࡰࡴࡷࡣࡸ࡮ࡡࠣᰡ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11111_opy_ (u"ࠨࡢࡳࡣࡱࡧ࡭ࠨᰢ"): repo.active_branch.name,
            bstack11111_opy_ (u"ࠢࡵࡣࡪࠦᰣ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࠦᰤ"): bstack111l11l1ll1_opy_(repo.head.commit.committer),
            bstack11111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࡤࡪࡡࡵࡧࠥᰥ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11111_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࠥᰦ"): bstack111l11l1ll1_opy_(repo.head.commit.author),
            bstack11111_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡣࡩࡧࡴࡦࠤᰧ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᰨ"): repo.head.commit.message,
            bstack11111_opy_ (u"ࠨࡲࡰࡱࡷࠦᰩ"): repo.git.rev_parse(bstack11111_opy_ (u"ࠢ࠮࠯ࡶ࡬ࡴࡽ࠭ࡵࡱࡳࡰࡪࡼࡥ࡭ࠤᰪ")),
            bstack11111_opy_ (u"ࠣࡥࡲࡱࡲࡵ࡮ࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᰫ"): bstack111l11lll11_opy_,
            bstack11111_opy_ (u"ࠤࡺࡳࡷࡱࡴࡳࡧࡨࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᰬ"): subprocess.check_output([bstack11111_opy_ (u"ࠥ࡫࡮ࡺࠢᰭ"), bstack11111_opy_ (u"ࠦࡷ࡫ࡶ࠮ࡲࡤࡶࡸ࡫ࠢᰮ"), bstack11111_opy_ (u"ࠧ࠳࠭ࡨ࡫ࡷ࠱ࡨࡵ࡭࡮ࡱࡱ࠱ࡩ࡯ࡲࠣᰯ")]).strip().decode(
                bstack11111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᰰ")),
            bstack11111_opy_ (u"ࠢ࡭ࡣࡶࡸࡤࡺࡡࡨࠤᰱ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡴࡡࡶ࡭ࡳࡩࡥࡠ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᰲ"): repo.git.rev_list(
                bstack11111_opy_ (u"ࠤࡾࢁ࠳࠴ࡻࡾࠤᰳ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l1ll1111_opy_ = []
        for remote in remotes:
            bstack1111l1l11ll_opy_ = {
                bstack11111_opy_ (u"ࠥࡲࡦࡳࡥࠣᰴ"): remote.name,
                bstack11111_opy_ (u"ࠦࡺࡸ࡬ࠣᰵ"): remote.url,
            }
            bstack111l1ll1111_opy_.append(bstack1111l1l11ll_opy_)
        bstack1111ll111l1_opy_ = {
            bstack11111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰶ"): bstack11111_opy_ (u"ࠨࡧࡪࡶ᰷ࠥ"),
            **info,
            bstack11111_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫ࡳࠣ᰸"): bstack111l1ll1111_opy_
        }
        bstack1111ll111l1_opy_ = bstack111l111111l_opy_(bstack1111ll111l1_opy_)
        return bstack1111ll111l1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦ᰹").format(err))
        return {}
def bstack11ll1l1l11l_opy_(bstack1111lll1ll1_opy_=None):
    bstack11111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡹࡰࡦࡥ࡬ࡪ࡮ࡩࡡ࡭࡮ࡼࠤ࡫ࡵࡲ࡮ࡣࡷࡸࡪࡪࠠࡧࡱࡵࠤࡆࡏࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡹࡸ࡫ࠠࡤࡣࡶࡩࡸࠦࡦࡰࡴࠣࡩࡦࡩࡨࠡࡨࡲࡰࡩ࡫ࡲࠡ࡫ࡱࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡫ࡵ࡬ࡥࡧࡵࡷࠥ࠮࡬ࡪࡵࡷ࠰ࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠩ࠻ࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡒࡴࡴࡥ࠻ࠢࡐࡳࡳࡵ࠭ࡳࡧࡳࡳࠥࡧࡰࡱࡴࡲࡥࡨ࡮ࠬࠡࡷࡶࡩࡸࠦࡣࡶࡴࡵࡩࡳࡺࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࡟ࡴࡹ࠮ࡨࡧࡷࡧࡼࡪࠨࠪ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡉࡲࡶࡴࡺࠢ࡯࡭ࡸࡺࠠ࡜࡟࠽ࠤࡒࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡻ࡮ࡺࡨࠡࡰࡲࠤࡸࡵࡵࡳࡥࡨࡷࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥ࠮ࠣࡶࡪࡺࡵࡳࡰࡶࠤࡠࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡲࡤࡸ࡭ࡹ࠺ࠡࡏࡸࡰࡹ࡯࠭ࡳࡧࡳࡳࠥࡧࡰࡱࡴࡲࡥࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥࡹࡰࡦࡥ࡬ࡪ࡮ࡩࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࡶࡲࠤࡦࡴࡡ࡭ࡻࡽࡩࠏࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡲࡩࡴࡶ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡪࡩࡤࡶࡶ࠰ࠥ࡫ࡡࡤࡪࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡰࡴࠣࡥࠥ࡬࡯࡭ࡦࡨࡶ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ᰺")
    if bstack1111lll1ll1_opy_ is None:
        bstack1111lll1ll1_opy_ = [os.getcwd()]
    elif isinstance(bstack1111lll1ll1_opy_, list) and len(bstack1111lll1ll1_opy_) == 0:
        return []
    results = []
    for folder in bstack1111lll1ll1_opy_:
        try:
            if not os.path.exists(folder):
                raise Exception(bstack11111_opy_ (u"ࠥࡊࡴࡲࡤࡦࡴࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠣ᰻").format(folder))
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11111_opy_ (u"ࠦࡵࡸࡉࡥࠤ᰼"): bstack11111_opy_ (u"ࠧࠨ᰽"),
                bstack11111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᰾"): [],
                bstack11111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣ᰿"): [],
                bstack11111_opy_ (u"ࠣࡲࡵࡈࡦࡺࡥࠣ᱀"): bstack11111_opy_ (u"ࠤࠥ᱁"),
                bstack11111_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦ᱂"): [],
                bstack11111_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧ᱃"): bstack11111_opy_ (u"ࠧࠨ᱄"),
                bstack11111_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨ᱅"): bstack11111_opy_ (u"ࠢࠣ᱆"),
                bstack11111_opy_ (u"ࠣࡲࡵࡖࡦࡽࡄࡪࡨࡩࠦ᱇"): bstack11111_opy_ (u"ࠤࠥ᱈")
            }
            bstack111l11l111l_opy_ = repo.active_branch.name
            bstack1111l1l1ll1_opy_ = repo.head.commit
            result[bstack11111_opy_ (u"ࠥࡴࡷࡏࡤࠣ᱉")] = bstack1111l1l1ll1_opy_.hexsha
            bstack111l1l111l1_opy_ = _1111lll1l11_opy_(repo)
            logger.debug(bstack11111_opy_ (u"ࠦࡇࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠽ࠤࠧ᱊") + str(bstack111l1l111l1_opy_) + bstack11111_opy_ (u"ࠧࠨ᱋"))
            if bstack111l1l111l1_opy_:
                try:
                    bstack111l11ll1ll_opy_ = repo.git.diff(bstack11111_opy_ (u"ࠨ࠭࠮ࡰࡤࡱࡪ࠳࡯࡯࡮ࡼࠦ᱌"), bstack1lll1l1l111_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧᱍ")).split(bstack11111_opy_ (u"ࠨ࡞ࡱࠫᱎ"))
                    logger.debug(bstack11111_opy_ (u"ࠤࡆ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡥࡩࡹࡽࡥࡦࡰࠣࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿࠣࡥࡳࡪࠠࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿ࠽ࠤࠧᱏ") + str(bstack111l11ll1ll_opy_) + bstack11111_opy_ (u"ࠥࠦ᱐"))
                    result[bstack11111_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥ᱑")] = [f.strip() for f in bstack111l11ll1ll_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1l1l111_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤ᱒")))
                except Exception:
                    logger.debug(bstack11111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠯ࠢࡉࡥࡱࡲࡩ࡯ࡩࠣࡦࡦࡩ࡫ࠡࡶࡲࠤࡷ࡫ࡣࡦࡰࡷࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠨ᱓"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11111_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᱔")] = _11111lllll1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11111_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢ᱕")] = _11111lllll1_opy_(commits[:5])
            bstack111l111ll1l_opy_ = set()
            bstack111l11lll1l_opy_ = []
            for commit in commits:
                logger.debug(bstack11111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰ࡭ࡹࡀࠠࠣ᱖") + str(commit.message) + bstack11111_opy_ (u"ࠥࠦ᱗"))
                bstack1111l1111l1_opy_ = commit.author.name if commit.author else bstack11111_opy_ (u"࡚ࠦࡴ࡫࡯ࡱࡺࡲࠧ᱘")
                bstack111l111ll1l_opy_.add(bstack1111l1111l1_opy_)
                bstack111l11lll1l_opy_.append({
                    bstack11111_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨ᱙"): commit.message.strip(),
                    bstack11111_opy_ (u"ࠨࡵࡴࡧࡵࠦᱚ"): bstack1111l1111l1_opy_
                })
            result[bstack11111_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᱛ")] = list(bstack111l111ll1l_opy_)
            result[bstack11111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤᱜ")] = bstack111l11lll1l_opy_
            result[bstack11111_opy_ (u"ࠤࡳࡶࡉࡧࡴࡦࠤᱝ")] = bstack1111l1l1ll1_opy_.committed_datetime.strftime(bstack11111_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨࠧᱞ"))
            if (not result[bstack11111_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᱟ")] or result[bstack11111_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᱠ")].strip() == bstack11111_opy_ (u"ࠨࠢᱡ")) and bstack1111l1l1ll1_opy_.message:
                bstack1111lll11ll_opy_ = bstack1111l1l1ll1_opy_.message.strip().splitlines()
                result[bstack11111_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᱢ")] = bstack1111lll11ll_opy_[0] if bstack1111lll11ll_opy_ else bstack11111_opy_ (u"ࠣࠤᱣ")
                if len(bstack1111lll11ll_opy_) > 2:
                    result[bstack11111_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤᱤ")] = bstack11111_opy_ (u"ࠪࡠࡳ࠭ᱥ").join(bstack1111lll11ll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࠫࡪࡴࡲࡤࡦࡴ࠽ࠤࢀࢃࠩ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᱦ").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _1111ll1ll1l_opy_(result)
    ]
    return filtered_results
def _1111ll1ll1l_opy_(result):
    bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡥ࡭ࡲࡨࡶࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡪࡨࠣࡥࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡮ࡹࠠࡷࡣ࡯࡭ࡩࠦࠨ࡯ࡱࡱ࠱ࡪࡳࡰࡵࡻࠣࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠢࡤࡲࡩࠦࡡࡶࡶ࡫ࡳࡷࡹࠩ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᱧ")
    return (
        isinstance(result.get(bstack11111_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᱨ"), None), list)
        and len(result[bstack11111_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᱩ")]) > 0
        and isinstance(result.get(bstack11111_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᱪ"), None), list)
        and len(result[bstack11111_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᱫ")]) > 0
    )
def _1111lll1l11_opy_(repo):
    bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡘࡷࡿࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡴࡩࡧࠣࡦࡦࡹࡥࠡࡤࡵࡥࡳࡩࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡴࡨࡴࡴࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡩࡣࡵࡨࡨࡵࡤࡦࡦࠣࡲࡦࡳࡥࡴࠢࡤࡲࡩࠦࡷࡰࡴ࡮ࠤࡼ࡯ࡴࡩࠢࡤࡰࡱࠦࡖࡄࡕࠣࡴࡷࡵࡶࡪࡦࡨࡶࡸ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣࡦࡷࡧ࡮ࡤࡪࠣ࡭࡫ࠦࡰࡰࡵࡶ࡭ࡧࡲࡥ࠭ࠢࡨࡰࡸ࡫ࠠࡏࡱࡱࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᱬ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111llll1l1_opy_ = origin.refs[bstack11111_opy_ (u"ࠫࡍࡋࡁࡅࠩᱭ")]
            target = bstack1111llll1l1_opy_.reference.name
            if target.startswith(bstack11111_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᱮ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11111_opy_ (u"࠭࡯ࡳ࡫ࡪ࡭ࡳ࠵ࠧᱯ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _11111lllll1_opy_(commits):
    bstack11111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᱰ")
    bstack111l11ll1ll_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111lll1lll_opy_ in diff:
                        if bstack1111lll1lll_opy_.a_path:
                            bstack111l11ll1ll_opy_.add(bstack1111lll1lll_opy_.a_path)
                        if bstack1111lll1lll_opy_.b_path:
                            bstack111l11ll1ll_opy_.add(bstack1111lll1lll_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l11ll1ll_opy_)
def bstack111l111111l_opy_(bstack1111ll111l1_opy_):
    bstack1111lllllll_opy_ = bstack1111l1l1l1l_opy_(bstack1111ll111l1_opy_)
    if bstack1111lllllll_opy_ and bstack1111lllllll_opy_ > bstack11l11l11l11_opy_:
        bstack111l1l1l1l1_opy_ = bstack1111lllllll_opy_ - bstack11l11l11l11_opy_
        bstack1111l1lll11_opy_ = bstack111l11l11l1_opy_(bstack1111ll111l1_opy_[bstack11111_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᱱ")], bstack111l1l1l1l1_opy_)
        bstack1111ll111l1_opy_[bstack11111_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᱲ")] = bstack1111l1lll11_opy_
        logger.info(bstack11111_opy_ (u"ࠥࡘ࡭࡫ࠠࡤࡱࡰࡱ࡮ࡺࠠࡩࡣࡶࠤࡧ࡫ࡥ࡯ࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨ࠳ࠦࡓࡪࡼࡨࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࠠࡢࡨࡷࡩࡷࠦࡴࡳࡷࡱࡧࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡻࡾࠢࡎࡆࠧᱳ")
                    .format(bstack1111l1l1l1l_opy_(bstack1111ll111l1_opy_) / 1024))
    return bstack1111ll111l1_opy_
def bstack1111l1l1l1l_opy_(json_data):
    try:
        if json_data:
            bstack1111lll11l1_opy_ = json.dumps(json_data)
            bstack1111l1l11l1_opy_ = sys.getsizeof(bstack1111lll11l1_opy_)
            return bstack1111l1l11l1_opy_
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡦࡲࡣࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡵ࡬ࡾࡪࠦ࡯ࡧࠢࡍࡗࡔࡔࠠࡰࡤ࡭ࡩࡨࡺ࠺ࠡࡽࢀࠦᱴ").format(e))
    return -1
def bstack111l11l11l1_opy_(field, bstack1111l1l1lll_opy_):
    try:
        bstack1111l11l111_opy_ = len(bytes(bstack11l1l111lll_opy_, bstack11111_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᱵ")))
        bstack1111lll111l_opy_ = bytes(field, bstack11111_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᱶ"))
        bstack1111l11lll1_opy_ = len(bstack1111lll111l_opy_)
        bstack111l11111ll_opy_ = ceil(bstack1111l11lll1_opy_ - bstack1111l1l1lll_opy_ - bstack1111l11l111_opy_)
        if bstack111l11111ll_opy_ > 0:
            bstack1111lll1l1l_opy_ = bstack1111lll111l_opy_[:bstack111l11111ll_opy_].decode(bstack11111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᱷ"), errors=bstack11111_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨᱸ")) + bstack11l1l111lll_opy_
            return bstack1111lll1l1l_opy_
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡴࡸࡲࡨࡧࡴࡪࡰࡪࠤ࡫࡯ࡥ࡭ࡦ࠯ࠤࡳࡵࡴࡩ࡫ࡱ࡫ࠥࡽࡡࡴࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨࠥ࡮ࡥࡳࡧ࠽ࠤࢀࢃࠢᱹ").format(e))
    return field
def bstack111l1ll11_opy_():
    env = os.environ
    if (bstack11111_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᱺ") in env and len(env[bstack11111_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤᱻ")]) > 0) or (
            bstack11111_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᱼ") in env and len(env[bstack11111_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧᱽ")]) > 0):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᱾"): bstack11111_opy_ (u"ࠣࡌࡨࡲࡰ࡯࡮ࡴࠤ᱿"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲀ"): env.get(bstack11111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᲁ")),
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲂ"): env.get(bstack11111_opy_ (u"ࠧࡐࡏࡃࡡࡑࡅࡒࡋࠢᲃ")),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲄ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲅ"))
        }
    if env.get(bstack11111_opy_ (u"ࠣࡅࡌࠦᲆ")) == bstack11111_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲇ") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡆࡍࠧᲈ"))):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲉ"): bstack11111_opy_ (u"ࠧࡉࡩࡳࡥ࡯ࡩࡈࡏࠢᲊ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲋"): env.get(bstack11111_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᲌")),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᲍"): env.get(bstack11111_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡍࡓࡇࠨ᲎")),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᲏"): env.get(bstack11111_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࠢᲐ"))
        }
    if env.get(bstack11111_opy_ (u"ࠧࡉࡉࠣᲑ")) == bstack11111_opy_ (u"ࠨࡴࡳࡷࡨࠦᲒ") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙ࠢᲓ"))):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᲔ"): bstack11111_opy_ (u"ࠤࡗࡶࡦࡼࡩࡴࠢࡆࡍࠧᲕ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲖ"): env.get(bstack11111_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢ࡛ࡊࡈ࡟ࡖࡔࡏࠦᲗ")),
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲘ"): env.get(bstack11111_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᲙ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲚ"): env.get(bstack11111_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲛ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤࡆࡍࠧᲜ")) == bstack11111_opy_ (u"ࠥࡸࡷࡻࡥࠣᲝ") and env.get(bstack11111_opy_ (u"ࠦࡈࡏ࡟ࡏࡃࡐࡉࠧᲞ")) == bstack11111_opy_ (u"ࠧࡩ࡯ࡥࡧࡶ࡬࡮ࡶࠢᲟ"):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲠ"): bstack11111_opy_ (u"ࠢࡄࡱࡧࡩࡸ࡮ࡩࡱࠤᲡ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲢ"): None,
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲣ"): None,
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲤ"): None
        }
    if env.get(bstack11111_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡔࡄࡒࡈࡎࠢᲥ")) and env.get(bstack11111_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡅࡒࡑࡒࡏࡔࠣᲦ")):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲧ"): bstack11111_opy_ (u"ࠢࡃ࡫ࡷࡦࡺࡩ࡫ࡦࡶࠥᲨ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲩ"): env.get(bstack11111_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡍࡉࡕࡡࡋࡘ࡙ࡖ࡟ࡐࡔࡌࡋࡎࡔࠢᲪ")),
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲫ"): None,
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲬ"): env.get(bstack11111_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲭ"))
        }
    if env.get(bstack11111_opy_ (u"ࠨࡃࡊࠤᲮ")) == bstack11111_opy_ (u"ࠢࡵࡴࡸࡩࠧᲯ") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠣࡆࡕࡓࡓࡋࠢᲰ"))):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲱ"): bstack11111_opy_ (u"ࠥࡈࡷࡵ࡮ࡦࠤᲲ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲳ"): env.get(bstack11111_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡐࡎࡔࡋࠣᲴ")),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲵ"): None,
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲶ"): env.get(bstack11111_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᲷ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤࡆࡍࠧᲸ")) == bstack11111_opy_ (u"ࠥࡸࡷࡻࡥࠣᲹ") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋࠢᲺ"))):
        return {
            bstack11111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᲻"): bstack11111_opy_ (u"ࠨࡓࡦ࡯ࡤࡴ࡭ࡵࡲࡦࠤ᲼"),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲽ"): env.get(bstack11111_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡔࡘࡇࡂࡐࡌ࡞ࡆ࡚ࡉࡐࡐࡢ࡙ࡗࡒࠢᲾ")),
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲿ"): env.get(bstack11111_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ᳀")),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳁"): env.get(bstack11111_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡏࡄࠣ᳂"))
        }
    if env.get(bstack11111_opy_ (u"ࠨࡃࡊࠤ᳃")) == bstack11111_opy_ (u"ࠢࡵࡴࡸࡩࠧ᳄") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠣࡉࡌࡘࡑࡇࡂࡠࡅࡌࠦ᳅"))):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳆"): bstack11111_opy_ (u"ࠥࡋ࡮ࡺࡌࡢࡤࠥ᳇"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᳈"): env.get(bstack11111_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤ࡛ࡒࡍࠤ᳉")),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳊"): env.get(bstack11111_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᳋")),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳌"): env.get(bstack11111_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡌࡈࠧ᳍"))
        }
    if env.get(bstack11111_opy_ (u"ࠥࡇࡎࠨ᳎")) == bstack11111_opy_ (u"ࠦࡹࡸࡵࡦࠤ᳏") and bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࠣ᳐"))):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳑"): bstack11111_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡱࡩࡵࡧࠥ᳒"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳓"): env.get(bstack11111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌ᳔ࠣ")),
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳕ࠧ"): env.get(bstack11111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡍࡃࡅࡉࡑࠨ᳖")) or env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅ᳗ࠣ")),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳘ࠧ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᳙"))
        }
    if bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥ᳚"))):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳛"): bstack11111_opy_ (u"࡚ࠥ࡮ࡹࡵࡢ࡮ࠣࡗࡹࡻࡤࡪࡱࠣࡘࡪࡧ࡭ࠡࡕࡨࡶࡻ࡯ࡣࡦࡵ᳜ࠥ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳝ࠢ"): bstack11111_opy_ (u"ࠧࢁࡽࡼࡿ᳞ࠥ").format(env.get(bstack11111_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊ᳟ࠩ")), env.get(bstack11111_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࡎࡊࠧ᳠"))),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳡"): env.get(bstack11111_opy_ (u"ࠤࡖ࡝ࡘ࡚ࡅࡎࡡࡇࡉࡋࡏࡎࡊࡖࡌࡓࡓࡏࡄ᳢ࠣ")),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack11111_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇ᳤ࠦ"))
        }
    if bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ᳥ࠢ"))):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳦ࠦ"): bstack11111_opy_ (u"ࠢࡂࡲࡳࡺࡪࡿ࡯ࡳࠤ᳧"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯᳨ࠦ"): bstack11111_opy_ (u"ࠤࡾࢁ࠴ࡶࡲࡰ࡬ࡨࡧࡹ࠵ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠣᳩ").format(env.get(bstack11111_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤ࡛ࡒࡍࠩᳪ")), env.get(bstack11111_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡁࡄࡅࡒ࡙ࡓ࡚࡟ࡏࡃࡐࡉࠬᳫ")), env.get(bstack11111_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡕࡏ࡙ࡌ࠭ᳬ")), env.get(bstack11111_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡊࡆ᳭ࠪ"))),
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᳮ"): env.get(bstack11111_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᳯ")),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᳰ"): env.get(bstack11111_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᳱ"))
        }
    if env.get(bstack11111_opy_ (u"ࠦࡆࡠࡕࡓࡇࡢࡌ࡙࡚ࡐࡠࡗࡖࡉࡗࡥࡁࡈࡇࡑࡘࠧᳲ")) and env.get(bstack11111_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᳳ")):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳴"): bstack11111_opy_ (u"ࠢࡂࡼࡸࡶࡪࠦࡃࡊࠤᳵ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᳶ"): bstack11111_opy_ (u"ࠤࡾࢁࢀࢃ࠯ࡠࡤࡸ࡭ࡱࡪ࠯ࡳࡧࡶࡹࡱࡺࡳࡀࡤࡸ࡭ࡱࡪࡉࡥ࠿ࡾࢁࠧ᳷").format(env.get(bstack11111_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭᳸")), env.get(bstack11111_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࠩ᳹")), env.get(bstack11111_opy_ (u"ࠬࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠬᳺ"))),
            bstack11111_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳻"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᳼")),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳽"): env.get(bstack11111_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ᳾"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣ᳿")), env.get(bstack11111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡓࡇࡖࡓࡑ࡜ࡅࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᴀ")), env.get(bstack11111_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᴁ"))]):
        return {
            bstack11111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴂ"): bstack11111_opy_ (u"ࠢࡂ࡙ࡖࠤࡈࡵࡤࡦࡄࡸ࡭ࡱࡪࠢᴃ"),
            bstack11111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴄ"): env.get(bstack11111_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡖࡕࡃࡎࡌࡇࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᴅ")),
            bstack11111_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴆ"): env.get(bstack11111_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᴇ")),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴈ"): env.get(bstack11111_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴉ"))
        }
    if env.get(bstack11111_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧᴊ")):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᴋ"): bstack11111_opy_ (u"ࠤࡅࡥࡲࡨ࡯ࡰࠤᴌ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴍ"): env.get(bstack11111_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡕࡩࡸࡻ࡬ࡵࡵࡘࡶࡱࠨᴎ")),
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴏ"): env.get(bstack11111_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡳࡩࡱࡵࡸࡏࡵࡢࡏࡣࡰࡩࠧᴐ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴑ"): env.get(bstack11111_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᴒ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࠥᴓ")) or env.get(bstack11111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧᴔ")):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴕ"): bstack11111_opy_ (u"ࠧ࡝ࡥࡳࡥ࡮ࡩࡷࠨᴖ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴗ"): env.get(bstack11111_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᴘ")),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴙ"): bstack11111_opy_ (u"ࠤࡐࡥ࡮ࡴࠠࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠤᴚ") if env.get(bstack11111_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧᴛ")) else None,
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴜ"): env.get(bstack11111_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡇࡊࡖࡢࡇࡔࡓࡍࡊࡖࠥᴝ"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠨࡇࡄࡒࡢࡔࡗࡕࡊࡆࡅࡗࠦᴞ")), env.get(bstack11111_opy_ (u"ࠢࡈࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣᴟ")), env.get(bstack11111_opy_ (u"ࠣࡉࡒࡓࡌࡒࡅࡠࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣᴠ"))]):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴡ"): bstack11111_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡇࡱࡵࡵࡥࠤᴢ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴣ"): None,
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴤ"): env.get(bstack11111_opy_ (u"ࠨࡐࡓࡑࡍࡉࡈ࡚࡟ࡊࡆࠥᴥ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴦ"): env.get(bstack11111_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴧ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࠧᴨ")):
        return {
            bstack11111_opy_ (u"ࠥࡲࡦࡳࡥࠣᴩ"): bstack11111_opy_ (u"ࠦࡘ࡮ࡩࡱࡲࡤࡦࡱ࡫ࠢᴪ"),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴫ"): env.get(bstack11111_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᴬ")),
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴭ"): bstack11111_opy_ (u"ࠣࡌࡲࡦࠥࠩࡻࡾࠤᴮ").format(env.get(bstack11111_opy_ (u"ࠩࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠬᴯ"))) if env.get(bstack11111_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉࠨᴰ")) else None,
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴱ"): env.get(bstack11111_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᴲ"))
        }
    if bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠨࡎࡆࡖࡏࡍࡋ࡟ࠢᴳ"))):
        return {
            bstack11111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴴ"): bstack11111_opy_ (u"ࠣࡐࡨࡸࡱ࡯ࡦࡺࠤᴵ"),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴶ"): env.get(bstack11111_opy_ (u"ࠥࡈࡊࡖࡌࡐ࡛ࡢ࡙ࡗࡒࠢᴷ")),
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴸ"): env.get(bstack11111_opy_ (u"࡙ࠧࡉࡕࡇࡢࡒࡆࡓࡅࠣᴹ")),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴺ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᴻ"))
        }
    if bstack1l1111l1ll_opy_(env.get(bstack11111_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡃࡆࡘࡎࡕࡎࡔࠤᴼ"))):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴽ"): bstack11111_opy_ (u"ࠥࡋ࡮ࡺࡈࡶࡤࠣࡅࡨࡺࡩࡰࡰࡶࠦᴾ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴿ"): bstack11111_opy_ (u"ࠧࢁࡽ࠰ࡽࢀ࠳ࡦࡩࡴࡪࡱࡱࡷ࠴ࡸࡵ࡯ࡵ࠲ࡿࢂࠨᵀ").format(env.get(bstack11111_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡓࡆࡔ࡙ࡉࡗࡥࡕࡓࡎࠪᵁ")), env.get(bstack11111_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡇࡓࡓࡘࡏࡔࡐࡔ࡜ࠫᵂ")), env.get(bstack11111_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠨᵃ"))),
            bstack11111_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᵄ"): env.get(bstack11111_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢ࡛ࡔࡘࡋࡇࡎࡒ࡛ࠧᵅ")),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᵆ"): env.get(bstack11111_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠧᵇ"))
        }
    if env.get(bstack11111_opy_ (u"ࠨࡃࡊࠤᵈ")) == bstack11111_opy_ (u"ࠢࡵࡴࡸࡩࠧᵉ") and env.get(bstack11111_opy_ (u"ࠣࡘࡈࡖࡈࡋࡌࠣᵊ")) == bstack11111_opy_ (u"ࠤ࠴ࠦᵋ"):
        return {
            bstack11111_opy_ (u"ࠥࡲࡦࡳࡥࠣᵌ"): bstack11111_opy_ (u"࡛ࠦ࡫ࡲࡤࡧ࡯ࠦᵍ"),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵎ"): bstack11111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࡻࡾࠤᵏ").format(env.get(bstack11111_opy_ (u"ࠧࡗࡇࡕࡇࡊࡒ࡟ࡖࡔࡏࠫᵐ"))),
            bstack11111_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵑ"): None,
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵒ"): None,
        }
    if env.get(bstack11111_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᵓ")):
        return {
            bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵔ"): bstack11111_opy_ (u"࡚ࠧࡥࡢ࡯ࡦ࡭ࡹࡿࠢᵕ"),
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵖ"): None,
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵗ"): env.get(bstack11111_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢࡔࡗࡕࡊࡆࡅࡗࡣࡓࡇࡍࡆࠤᵘ")),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵙ"): env.get(bstack11111_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᵚ"))
        }
    if any([env.get(bstack11111_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋࠢᵛ")), env.get(bstack11111_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡕࡐࠧᵜ")), env.get(bstack11111_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡗࡊࡘࡎࡂࡏࡈࠦᵝ")), env.get(bstack11111_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢࡘࡊࡇࡍࠣᵞ"))]):
        return {
            bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᵟ"): bstack11111_opy_ (u"ࠤࡆࡳࡳࡩ࡯ࡶࡴࡶࡩࠧᵠ"),
            bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᵡ"): None,
            bstack11111_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᵢ"): env.get(bstack11111_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᵣ")) or None,
            bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᵤ"): env.get(bstack11111_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᵥ"), 0)
        }
    if env.get(bstack11111_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᵦ")):
        return {
            bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᵧ"): bstack11111_opy_ (u"ࠥࡋࡴࡉࡄࠣᵨ"),
            bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᵩ"): None,
            bstack11111_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᵪ"): env.get(bstack11111_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᵫ")),
            bstack11111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᵬ"): env.get(bstack11111_opy_ (u"ࠣࡉࡒࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡃࡐࡗࡑࡘࡊࡘࠢᵭ"))
        }
    if env.get(bstack11111_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᵮ")):
        return {
            bstack11111_opy_ (u"ࠥࡲࡦࡳࡥࠣᵯ"): bstack11111_opy_ (u"ࠦࡈࡵࡤࡦࡈࡵࡩࡸ࡮ࠢᵰ"),
            bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵱ"): env.get(bstack11111_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᵲ")),
            bstack11111_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵳ"): env.get(bstack11111_opy_ (u"ࠣࡅࡉࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᵴ")),
            bstack11111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵵ"): env.get(bstack11111_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᵶ"))
        }
    return {bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᵷ"): None}
def get_host_info():
    return {
        bstack11111_opy_ (u"ࠧ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠢᵸ"): platform.node(),
        bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣᵹ"): platform.system(),
        bstack11111_opy_ (u"ࠢࡵࡻࡳࡩࠧᵺ"): platform.machine(),
        bstack11111_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤᵻ"): platform.version(),
        bstack11111_opy_ (u"ࠤࡤࡶࡨ࡮ࠢᵼ"): platform.architecture()[0]
    }
def bstack11l111lll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l11llll1_opy_():
    if bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫᵽ")):
        return bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᵾ")
    return bstack11111_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠫᵿ")
def bstack1111ll1lll1_opy_(driver):
    info = {
        bstack11111_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᶀ"): driver.capabilities,
        bstack11111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫᶁ"): driver.session_id,
        bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩᶂ"): driver.capabilities.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᶃ"), None),
        bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᶄ"): driver.capabilities.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᶅ"), None),
        bstack11111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࠧᶆ"): driver.capabilities.get(bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬᶇ"), None),
        bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪᶈ"):driver.capabilities.get(bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᶉ"), None),
    }
    if bstack111l11llll1_opy_() == bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᶊ"):
        if bstack11l1ll11l1_opy_():
            info[bstack11111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᶋ")] = bstack11111_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪᶌ")
        elif driver.capabilities.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᶍ"), {}).get(bstack11111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᶎ"), False):
            info[bstack11111_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᶏ")] = bstack11111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᶐ")
        else:
            info[bstack11111_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᶑ")] = bstack11111_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᶒ")
    return info
def bstack11l1ll11l1_opy_():
    if bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪᶓ")):
        return True
    if bstack1l1111l1ll_opy_(os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ᶔ"), None)):
        return True
    return False
def bstack1111ll1lll_opy_(bstack1111l111ll1_opy_, url, data, config):
    headers = config.get(bstack11111_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᶕ"), None)
    proxies = bstack111l11l1l1_opy_(config, url)
    auth = config.get(bstack11111_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᶖ"), None)
    response = requests.request(
            bstack1111l111ll1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1l1l11ll_opy_(bstack1ll1l1l111_opy_, size):
    bstack11ll1l1111_opy_ = []
    while len(bstack1ll1l1l111_opy_) > size:
        bstack1ll1ll1ll1_opy_ = bstack1ll1l1l111_opy_[:size]
        bstack11ll1l1111_opy_.append(bstack1ll1ll1ll1_opy_)
        bstack1ll1l1l111_opy_ = bstack1ll1l1l111_opy_[size:]
    bstack11ll1l1111_opy_.append(bstack1ll1l1l111_opy_)
    return bstack11ll1l1111_opy_
def bstack1111ll1ll11_opy_(message, bstack111l11lllll_opy_=False):
    os.write(1, bytes(message, bstack11111_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᶗ")))
    os.write(1, bytes(bstack11111_opy_ (u"ࠩ࡟ࡲࠬᶘ"), bstack11111_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᶙ")))
    if bstack111l11lllll_opy_:
        with open(bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡴ࠷࠱ࡺ࠯ࠪᶚ") + os.environ[bstack11111_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᶛ")] + bstack11111_opy_ (u"࠭࠮࡭ࡱࡪࠫᶜ"), bstack11111_opy_ (u"ࠧࡢࠩᶝ")) as f:
            f.write(message + bstack11111_opy_ (u"ࠨ࡞ࡱࠫᶞ"))
def bstack1lll11ll11l_opy_():
    return os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᶟ")].lower() == bstack11111_opy_ (u"ࠪࡸࡷࡻࡥࠨᶠ")
def bstack1l1lll11_opy_():
    return bstack1lll11ll_opy_().replace(tzinfo=None).isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭ᶡ")
def bstack111l11ll111_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11111_opy_ (u"ࠬࡠࠧᶢ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11111_opy_ (u"࡚࠭ࠨᶣ")))).total_seconds() * 1000
def bstack1111ll1l1ll_opy_(timestamp):
    return bstack111l111llll_opy_(timestamp).isoformat() + bstack11111_opy_ (u"࡛ࠧࠩᶤ")
def bstack111l1l11l11_opy_(bstack111l1l11111_opy_):
    date_format = bstack11111_opy_ (u"ࠨࠧ࡜ࠩࡲࠫࡤࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫࠭ᶥ")
    bstack1111l111l11_opy_ = datetime.datetime.strptime(bstack111l1l11111_opy_, date_format)
    return bstack1111l111l11_opy_.isoformat() + bstack11111_opy_ (u"ࠩ࡝ࠫᶦ")
def bstack1111l11ll1l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶧ")
    else:
        return bstack11111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᶨ")
def bstack1l1111l1ll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11111_opy_ (u"ࠬࡺࡲࡶࡧࠪᶩ")
def bstack1111ll1l1l1_opy_(val):
    return val.__str__().lower() == bstack11111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬᶪ")
def error_handler(bstack1111llll111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111llll111_opy_ as e:
                print(bstack11111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᶫ").format(func.__name__, bstack1111llll111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll11ll1_opy_(bstack111l1l11lll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1l11lll_opy_(cls, *args, **kwargs)
            except bstack1111llll111_opy_ as e:
                print(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣᶬ").format(bstack111l1l11lll_opy_.__name__, bstack1111llll111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll11ll1_opy_
    else:
        return decorator
def bstack1l1lll1ll_opy_(bstack1lll11l11_opy_):
    if os.getenv(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᶭ")) is not None:
        return bstack1l1111l1ll_opy_(os.getenv(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᶮ")))
    if bstack11111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᶯ") in bstack1lll11l11_opy_ and bstack1111ll1l1l1_opy_(bstack1lll11l11_opy_[bstack11111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶰ")]):
        return False
    if bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᶱ") in bstack1lll11l11_opy_ and bstack1111ll1l1l1_opy_(bstack1lll11l11_opy_[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶲ")]):
        return False
    return True
def bstack11l111ll1l_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111ll1llll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠣᶳ"), None)
        return bstack1111ll1llll_opy_ is None or bstack1111ll1llll_opy_ == bstack11111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᶴ")
    except Exception as e:
        return False
def bstack1111l1ll11_opy_(hub_url, CONFIG):
    if bstack1l1llllll_opy_() <= version.parse(bstack11111_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪᶵ")):
        if hub_url:
            return bstack11111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᶶ") + hub_url + bstack11111_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤᶷ")
        return bstack111l11ll11_opy_
    if hub_url:
        return bstack11111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᶸ") + hub_url + bstack11111_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣᶹ")
    return bstack111l1111l_opy_
def bstack111l1111ll1_opy_():
    return isinstance(os.getenv(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧᶺ")), str)
def bstack1l111l11l1_opy_(url):
    return urlparse(url).hostname
def bstack1ll11l1ll1_opy_(hostname):
    for bstack11ll1l1l11_opy_ in bstack11l11ll111_opy_:
        regex = re.compile(bstack11ll1l1l11_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l1lllll11_opy_(bstack111l111l11l_opy_, file_name, logger):
    bstack111111llll_opy_ = os.path.join(os.path.expanduser(bstack11111_opy_ (u"ࠩࢁࠫᶻ")), bstack111l111l11l_opy_)
    try:
        if not os.path.exists(bstack111111llll_opy_):
            os.makedirs(bstack111111llll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11111_opy_ (u"ࠪࢂࠬᶼ")), bstack111l111l11l_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11111_opy_ (u"ࠫࡼ࠭ᶽ")):
                pass
            with open(file_path, bstack11111_opy_ (u"ࠧࡽࠫࠣᶾ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111l111ll1_opy_.format(str(e)))
def bstack11l1lllll1l_opy_(file_name, key, value, logger):
    file_path = bstack11l1lllll11_opy_(bstack11111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᶿ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1ll1l1l_opy_ = json.load(open(file_path, bstack11111_opy_ (u"ࠧࡳࡤࠪ᷀")))
        else:
            bstack1l1ll1l1l_opy_ = {}
        bstack1l1ll1l1l_opy_[key] = value
        with open(file_path, bstack11111_opy_ (u"ࠣࡹ࠮ࠦ᷁")) as outfile:
            json.dump(bstack1l1ll1l1l_opy_, outfile)
def bstack1l111l11l_opy_(file_name, logger):
    file_path = bstack11l1lllll11_opy_(bstack11111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬᷂ࠩ"), file_name, logger)
    bstack1l1ll1l1l_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11111_opy_ (u"ࠪࡶࠬ᷃")) as bstack1111lllll_opy_:
            bstack1l1ll1l1l_opy_ = json.load(bstack1111lllll_opy_)
    return bstack1l1ll1l1l_opy_
def bstack1lll11l1ll_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࡀࠠࠨ᷄") + file_path + bstack11111_opy_ (u"ࠬࠦࠧ᷅") + str(e))
def bstack1l1llllll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11111_opy_ (u"ࠨ࠼ࡏࡑࡗࡗࡊ࡚࠾ࠣ᷆")
def bstack1l1lll1lll_opy_(config):
    if bstack11111_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭᷇") in config:
        del (config[bstack11111_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ᷈")])
        return False
    if bstack1l1llllll_opy_() < version.parse(bstack11111_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨ᷉")):
        return False
    if bstack1l1llllll_opy_() >= version.parse(bstack11111_opy_ (u"ࠪ࠸࠳࠷࠮࠶᷊ࠩ")):
        return True
    if bstack11111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ᷋") in config and config[bstack11111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ᷌")] is False:
        return False
    else:
        return True
def bstack11ll1lll1l_opy_(args_list, bstack111l11l1l1l_opy_):
    index = -1
    for value in bstack111l11l1l1l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack111l111l111_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack111l111l111_opy_(a[k], v)
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
        return Result(result=bstack11111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᷍"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ᷎ࠧ"), exception=exception)
    def bstack11111111ll_opy_(self):
        if self.result != bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᷏"):
            return None
        if isinstance(self.exception_type, str) and bstack11111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲ᷐ࠧ") in self.exception_type:
            return bstack11111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ᷑")
        return bstack11111_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ᷒")
    def bstack111l1l11l1l_opy_(self):
        if self.result != bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᷓ"):
            return None
        if self.bstack1l11l11l_opy_:
            return self.bstack1l11l11l_opy_
        return bstack1111l1l1111_opy_(self.exception)
def bstack1111l1l1111_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l11l11l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1lll1lll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11lllll1l1_opy_(config, logger):
    try:
        import playwright
        bstack111l1l1l1ll_opy_ = playwright.__file__
        bstack111l11l11ll_opy_ = os.path.split(bstack111l1l1l1ll_opy_)
        bstack111l1l1ll11_opy_ = bstack111l11l11ll_opy_[0] + bstack11111_opy_ (u"࠭࠯ࡥࡴ࡬ࡺࡪࡸ࠯ࡱࡣࡦ࡯ࡦ࡭ࡥ࠰࡮࡬ࡦ࠴ࡩ࡬ࡪ࠱ࡦࡰ࡮࠴ࡪࡴࠩᷔ")
        os.environ[bstack11111_opy_ (u"ࠧࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠪᷕ")] = bstack1lll11l11l_opy_(config)
        with open(bstack111l1l1ll11_opy_, bstack11111_opy_ (u"ࠨࡴࠪᷖ")) as f:
            file_content = f.read()
            bstack111l1l1l111_opy_ = bstack11111_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨᷗ")
            bstack111l1l1l11l_opy_ = file_content.find(bstack111l1l1l111_opy_)
            if bstack111l1l1l11l_opy_ == -1:
              process = subprocess.Popen(bstack11111_opy_ (u"ࠥࡲࡵࡳࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠢᷘ"), shell=True, cwd=bstack111l11l11ll_opy_[0])
              process.wait()
              bstack111l11l1111_opy_ = bstack11111_opy_ (u"ࠫࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵࠤ࠾ࠫᷙ")
              bstack111l1l1llll_opy_ = bstack11111_opy_ (u"ࠧࠨࠢࠡ࡞ࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺ࡜ࠣ࠽ࠣࡧࡴࡴࡳࡵࠢࡾࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠠࡾࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬ࠯࠻ࠡ࡫ࡩࠤ࠭ࡶࡲࡰࡥࡨࡷࡸ࠴ࡥ࡯ࡸ࠱ࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠯ࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠫ࠭ࡀࠦࠢࠣࠤᷚ")
              bstack1111l111111_opy_ = file_content.replace(bstack111l11l1111_opy_, bstack111l1l1llll_opy_)
              with open(bstack111l1l1ll11_opy_, bstack11111_opy_ (u"࠭ࡷࠨᷛ")) as f:
                f.write(bstack1111l111111_opy_)
    except Exception as e:
        logger.error(bstack1l111l11ll_opy_.format(str(e)))
def bstack1l1l11l1l1_opy_():
  try:
    bstack111l11111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᷜ"))
    bstack111l1l111ll_opy_ = []
    if os.path.exists(bstack111l11111l1_opy_):
      with open(bstack111l11111l1_opy_) as f:
        bstack111l1l111ll_opy_ = json.load(f)
      os.remove(bstack111l11111l1_opy_)
    return bstack111l1l111ll_opy_
  except:
    pass
  return []
def bstack111lll11ll_opy_(bstack11lll1llll_opy_):
  try:
    bstack111l1l111ll_opy_ = []
    bstack111l11111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᷝ"))
    if os.path.exists(bstack111l11111l1_opy_):
      with open(bstack111l11111l1_opy_) as f:
        bstack111l1l111ll_opy_ = json.load(f)
    bstack111l1l111ll_opy_.append(bstack11lll1llll_opy_)
    with open(bstack111l11111l1_opy_, bstack11111_opy_ (u"ࠩࡺࠫᷞ")) as f:
        json.dump(bstack111l1l111ll_opy_, f)
  except:
    pass
def bstack11ll1l1ll_opy_(logger, bstack111l1111l1l_opy_ = False):
  try:
    test_name = os.environ.get(bstack11111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭ᷟ"), bstack11111_opy_ (u"ࠫࠬᷠ"))
    if test_name == bstack11111_opy_ (u"ࠬ࠭ᷡ"):
        test_name = threading.current_thread().__dict__.get(bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡈࡤࡥࡡࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠬᷢ"), bstack11111_opy_ (u"ࠧࠨᷣ"))
    bstack111l11ll1l1_opy_ = bstack11111_opy_ (u"ࠨ࠮ࠣࠫᷤ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1111l1l_opy_:
        bstack11ll11lll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᷥ"), bstack11111_opy_ (u"ࠪ࠴ࠬᷦ"))
        bstack111111lll_opy_ = {bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᷧ"): test_name, bstack11111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷨ"): bstack111l11ll1l1_opy_, bstack11111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷩ"): bstack11ll11lll_opy_}
        bstack111l1111l11_opy_ = []
        bstack111l111l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᷪ"))
        if os.path.exists(bstack111l111l1ll_opy_):
            with open(bstack111l111l1ll_opy_) as f:
                bstack111l1111l11_opy_ = json.load(f)
        bstack111l1111l11_opy_.append(bstack111111lll_opy_)
        with open(bstack111l111l1ll_opy_, bstack11111_opy_ (u"ࠨࡹࠪᷫ")) as f:
            json.dump(bstack111l1111l11_opy_, f)
    else:
        bstack111111lll_opy_ = {bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᷬ"): test_name, bstack11111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᷭ"): bstack111l11ll1l1_opy_, bstack11111_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᷮ"): str(multiprocessing.current_process().name)}
        if bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩᷯ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack111111lll_opy_)
  except Exception as e:
      logger.warn(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡲࡼࡸࡪࡹࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᷰ").format(e))
def bstack1ll11ll1l_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11111_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪᷱ"))
    try:
      bstack1111ll11111_opy_ = []
      bstack111111lll_opy_ = {bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᷲ"): test_name, bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᷳ"): error_message, bstack11111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᷴ"): index}
      bstack1111l1ll1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ᷵"))
      if os.path.exists(bstack1111l1ll1l1_opy_):
          with open(bstack1111l1ll1l1_opy_) as f:
              bstack1111ll11111_opy_ = json.load(f)
      bstack1111ll11111_opy_.append(bstack111111lll_opy_)
      with open(bstack1111l1ll1l1_opy_, bstack11111_opy_ (u"ࠬࡽࠧ᷶")) as f:
          json.dump(bstack1111ll11111_opy_, f)
    except Exception as e:
      logger.warn(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤ᷷").format(e))
    return
  bstack1111ll11111_opy_ = []
  bstack111111lll_opy_ = {bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩ᷸ࠬ"): test_name, bstack11111_opy_ (u"ࠨࡧࡵࡶࡴࡸ᷹ࠧ"): error_message, bstack11111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ᷺"): index}
  bstack1111l1ll1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ᷻"))
  lock_file = bstack1111l1ll1l1_opy_ + bstack11111_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪ᷼")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1ll1l1_opy_):
          with open(bstack1111l1ll1l1_opy_, bstack11111_opy_ (u"ࠬࡸ᷽ࠧ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111ll11111_opy_ = json.load(open(bstack1111l1ll1l1_opy_))
      bstack1111ll11111_opy_.append(bstack111111lll_opy_)
      with open(bstack1111l1ll1l1_opy_, bstack11111_opy_ (u"࠭ࡷࠨ᷾")) as f:
          json.dump(bstack1111ll11111_opy_, f)
  except Exception as e:
    logger.warn(bstack11111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩ࠽ࠤࢀࢃ᷿ࠢ").format(e))
def bstack11l1lll1ll_opy_(bstack1l1111l111_opy_, name, logger):
  try:
    bstack111111lll_opy_ = {bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ḁ"): name, bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨḁ"): bstack1l1111l111_opy_, bstack11111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩḂ"): str(threading.current_thread()._name)}
    return bstack111111lll_opy_
  except Exception as e:
    logger.warn(bstack11111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡢࡦࡪࡤࡺࡪࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣḃ").format(e))
  return
def bstack1111ll11l1l_opy_():
    return platform.system() == bstack11111_opy_ (u"ࠬ࡝ࡩ࡯ࡦࡲࡻࡸ࠭Ḅ")
def bstack111ll1l1l_opy_(bstack1111l1ll1ll_opy_, config, logger):
    bstack1111l1l111l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111l1ll1ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡱࡺࡥࡳࠢࡦࡳࡳ࡬ࡩࡨࠢ࡮ࡩࡾࡹࠠࡣࡻࠣࡶࡪ࡭ࡥࡹࠢࡰࡥࡹࡩࡨ࠻ࠢࡾࢁࠧḅ").format(e))
    return bstack1111l1l111l_opy_
def bstack11l1l1l11l1_opy_(bstack1111ll11lll_opy_, bstack1111lllll1l_opy_):
    bstack1111ll11l11_opy_ = version.parse(bstack1111ll11lll_opy_)
    bstack1111l1llll1_opy_ = version.parse(bstack1111lllll1l_opy_)
    if bstack1111ll11l11_opy_ > bstack1111l1llll1_opy_:
        return 1
    elif bstack1111ll11l11_opy_ < bstack1111l1llll1_opy_:
        return -1
    else:
        return 0
def bstack1lll11ll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l111llll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll1l111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll1ll1l1_opy_(options, framework, config, bstack1l11ll1ll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11111_opy_ (u"ࠧࡨࡧࡷࠫḆ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11l111111_opy_ = caps.get(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩḇ"))
    bstack1111l11llll_opy_ = True
    bstack1ll1lllll1_opy_ = os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧḈ")]
    bstack1l111l11111_opy_ = config.get(bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪḉ"), False)
    if bstack1l111l11111_opy_:
        bstack1l11ll111l1_opy_ = config.get(bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḊ"), {})
        bstack1l11ll111l1_opy_[bstack11111_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨḋ")] = os.getenv(bstack11111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫḌ"))
        bstack1111ll111ll_opy_ = json.loads(os.getenv(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨḍ"), bstack11111_opy_ (u"ࠨࡽࢀࠫḎ"))).get(bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪḏ"))
    if bstack1111ll1l1l1_opy_(caps.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪ࡝࠳ࡄࠩḐ"))) or bstack1111ll1l1l1_opy_(caps.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫḑ"))):
        bstack1111l11llll_opy_ = False
    if bstack1l1lll1lll_opy_({bstack11111_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧḒ"): bstack1111l11llll_opy_}):
        bstack11l111111_opy_ = bstack11l111111_opy_ or {}
        bstack11l111111_opy_[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨḓ")] = bstack1111ll1l111_opy_(framework)
        bstack11l111111_opy_[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩḔ")] = bstack1lll11ll11l_opy_()
        bstack11l111111_opy_[bstack11111_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫḕ")] = bstack1ll1lllll1_opy_
        bstack11l111111_opy_[bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫḖ")] = bstack1l11ll1ll1_opy_
        if bstack1l111l11111_opy_:
            bstack11l111111_opy_[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪḗ")] = bstack1l111l11111_opy_
            bstack11l111111_opy_[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḘ")] = bstack1l11ll111l1_opy_
            bstack11l111111_opy_[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬḙ")][bstack11111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧḚ")] = bstack1111ll111ll_opy_
        if getattr(options, bstack11111_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨḛ"), None):
            options.set_capability(bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩḜ"), bstack11l111111_opy_)
        else:
            options[bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪḝ")] = bstack11l111111_opy_
    else:
        if getattr(options, bstack11111_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫḞ"), None):
            options.set_capability(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬḟ"), bstack1111ll1l111_opy_(framework))
            options.set_capability(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭Ḡ"), bstack1lll11ll11l_opy_())
            options.set_capability(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨḡ"), bstack1ll1lllll1_opy_)
            options.set_capability(bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨḢ"), bstack1l11ll1ll1_opy_)
            if bstack1l111l11111_opy_:
                options.set_capability(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧḣ"), bstack1l111l11111_opy_)
                options.set_capability(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨḤ"), bstack1l11ll111l1_opy_)
                options.set_capability(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴ࠰ࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪḥ"), bstack1111ll111ll_opy_)
        else:
            options[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬḦ")] = bstack1111ll1l111_opy_(framework)
            options[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ḧ")] = bstack1lll11ll11l_opy_()
            options[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨḨ")] = bstack1ll1lllll1_opy_
            options[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨḩ")] = bstack1l11ll1ll1_opy_
            if bstack1l111l11111_opy_:
                options[bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧḪ")] = bstack1l111l11111_opy_
                options[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨḫ")] = bstack1l11ll111l1_opy_
                options[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩḬ")][bstack11111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬḭ")] = bstack1111ll111ll_opy_
    return options
def bstack1111l1111ll_opy_(ws_endpoint, framework):
    bstack1l11ll1ll1_opy_ = bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢḮ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11111_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬḯ"))) > 1:
        ws_url = ws_endpoint.split(bstack11111_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭Ḱ"))[0]
        if bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫḱ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l111l1l1_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11111_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḲ"))[1]))
            bstack111l111l1l1_opy_ = bstack111l111l1l1_opy_ or {}
            bstack1ll1lllll1_opy_ = os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨḳ")]
            bstack111l111l1l1_opy_[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬḴ")] = str(framework) + str(__version__)
            bstack111l111l1l1_opy_[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ḵ")] = bstack1lll11ll11l_opy_()
            bstack111l111l1l1_opy_[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨḶ")] = bstack1ll1lllll1_opy_
            bstack111l111l1l1_opy_[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨḷ")] = bstack1l11ll1ll1_opy_
            ws_endpoint = ws_endpoint.split(bstack11111_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḸ"))[0] + bstack11111_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḹ") + urllib.parse.quote(json.dumps(bstack111l111l1l1_opy_))
    return ws_endpoint
def bstack1l11l1l11l_opy_():
    global bstack1l111lll1l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l111lll1l_opy_ = BrowserType.connect
    return bstack1l111lll1l_opy_
def bstack11llll111_opy_(framework_name):
    global bstack1111ll111l_opy_
    bstack1111ll111l_opy_ = framework_name
    return framework_name
def bstack11ll1l11l_opy_(self, *args, **kwargs):
    global bstack1l111lll1l_opy_
    try:
        global bstack1111ll111l_opy_
        if bstack11111_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧḺ") in kwargs:
            kwargs[bstack11111_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨḻ")] = bstack1111l1111ll_opy_(
                kwargs.get(bstack11111_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩḼ"), None),
                bstack1111ll111l_opy_
            )
    except Exception as e:
        logger.error(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨḽ").format(str(e)))
    return bstack1l111lll1l_opy_(self, *args, **kwargs)
def bstack1111l1lll1l_opy_(bstack1111llll11l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack111l11l1l1_opy_(bstack1111llll11l_opy_, bstack11111_opy_ (u"ࠢࠣḾ"))
        if proxies and proxies.get(bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢḿ")):
            parsed_url = urlparse(proxies.get(bstack11111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣṀ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ṁ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧṂ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11111_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨṃ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩṄ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l11l1lll1_opy_(bstack1111llll11l_opy_):
    bstack111l1l1lll1_opy_ = {
        bstack11l11l1l1l1_opy_[bstack111l1l11ll1_opy_]: bstack1111llll11l_opy_[bstack111l1l11ll1_opy_]
        for bstack111l1l11ll1_opy_ in bstack1111llll11l_opy_
        if bstack111l1l11ll1_opy_ in bstack11l11l1l1l1_opy_
    }
    bstack111l1l1lll1_opy_[bstack11111_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢṅ")] = bstack1111l1lll1l_opy_(bstack1111llll11l_opy_, bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣṆ")))
    bstack111l111lll1_opy_ = [element.lower() for element in bstack11l11l11ll1_opy_]
    bstack1111lll1111_opy_(bstack111l1l1lll1_opy_, bstack111l111lll1_opy_)
    return bstack111l1l1lll1_opy_
def bstack1111lll1111_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11111_opy_ (u"ࠤ࠭࠮࠯࠰ࠢṇ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111lll1111_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111lll1111_opy_(item, keys)
def bstack1ll1l111l11_opy_():
    bstack1111llll1ll_opy_ = [os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡍࡑࡋࡓࡠࡆࡌࡖࠧṈ")), os.path.join(os.path.expanduser(bstack11111_opy_ (u"ࠦࢃࠨṉ")), bstack11111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬṊ")), os.path.join(bstack11111_opy_ (u"࠭࠯ࡵ࡯ࡳࠫṋ"), bstack11111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧṌ"))]
    for path in bstack1111llll1ll_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11111_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣṍ") + str(path) + bstack11111_opy_ (u"ࠤࠪࠤࡪࡾࡩࡴࡶࡶ࠲ࠧṎ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11111_opy_ (u"ࠥࡋ࡮ࡼࡩ࡯ࡩࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠡࡨࡲࡶࠥ࠭ࠢṏ") + str(path) + bstack11111_opy_ (u"ࠦࠬࠨṐ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11111_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࠫࠧṑ") + str(path) + bstack11111_opy_ (u"ࠨࠧࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡫ࡥࡸࠦࡴࡩࡧࠣࡶࡪࡷࡵࡪࡴࡨࡨࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵ࠱ࠦṒ"))
            else:
                logger.debug(bstack11111_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࠨࠤṓ") + str(path) + bstack11111_opy_ (u"ࠣࠩࠣࡻ࡮ࡺࡨࠡࡹࡵ࡭ࡹ࡫ࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱ࠲ࠧṔ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11111_opy_ (u"ࠤࡒࡴࡪࡸࡡࡵ࡫ࡲࡲࠥࡹࡵࡤࡥࡨࡩࡩ࡫ࡤࠡࡨࡲࡶࠥ࠭ࠢṕ") + str(path) + bstack11111_opy_ (u"ࠥࠫ࠳ࠨṖ"))
            return path
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡺࡶࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡱࡣࡷ࡬ࢂ࠭࠺ࠡࠤṗ") + str(e) + bstack11111_opy_ (u"ࠧࠨṘ"))
    logger.debug(bstack11111_opy_ (u"ࠨࡁ࡭࡮ࠣࡴࡦࡺࡨࡴࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠥṙ"))
    return None
@measure(event_name=EVENTS.bstack11l11l111ll_opy_, stage=STAGE.bstack111l1l11l_opy_)
def bstack1l1l1llll11_opy_(binary_path, bstack1l11lll1l11_opy_, bs_config):
    logger.debug(bstack11111_opy_ (u"ࠢࡄࡷࡵࡶࡪࡴࡴࠡࡅࡏࡍࠥࡖࡡࡵࡪࠣࡪࡴࡻ࡮ࡥ࠼ࠣࡿࢂࠨṚ").format(binary_path))
    bstack111l1111lll_opy_ = bstack11111_opy_ (u"ࠨࠩṛ")
    bstack1111l111l1l_opy_ = {
        bstack11111_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧṜ"): __version__,
        bstack11111_opy_ (u"ࠥࡳࡸࠨṝ"): platform.system(),
        bstack11111_opy_ (u"ࠦࡴࡹ࡟ࡢࡴࡦ࡬ࠧṞ"): platform.machine(),
        bstack11111_opy_ (u"ࠧࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠥṟ"): bstack11111_opy_ (u"࠭࠰ࠨṠ"),
        bstack11111_opy_ (u"ࠢࡴࡦ࡮ࡣࡱࡧ࡮ࡨࡷࡤ࡫ࡪࠨṡ"): bstack11111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨṢ")
    }
    bstack1111ll1111l_opy_(bstack1111l111l1l_opy_)
    try:
        if binary_path:
            if bstack1111ll11l1l_opy_():
                bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧṣ")] = subprocess.check_output([binary_path, bstack11111_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦṤ")]).strip().decode(bstack11111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪṥ"))
            else:
                bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪṦ")] = subprocess.check_output([binary_path, bstack11111_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢṧ")], stderr=subprocess.DEVNULL).strip().decode(bstack11111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭Ṩ"))
        response = requests.request(
            bstack11111_opy_ (u"ࠨࡉࡈࡘࠬṩ"),
            url=bstack1ll11llll_opy_(bstack11l11l11l1l_opy_),
            headers=None,
            auth=(bs_config[bstack11111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫṪ")], bs_config[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ṫ")]),
            json=None,
            params=bstack1111l111l1l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11111_opy_ (u"ࠫࡺࡸ࡬ࠨṬ") in data.keys() and bstack11111_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫṭ") in data.keys():
            logger.debug(bstack11111_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢṮ").format(bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬṯ")]))
            if bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫṰ") in os.environ:
                logger.debug(bstack11111_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡡࡴࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠥ࡯ࡳࠡࡵࡨࡸࠧṱ"))
                data[bstack11111_opy_ (u"ࠪࡹࡷࡲࠧṲ")] = os.environ[bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧṳ")]
            bstack1111l1ll111_opy_ = bstack1111l11111l_opy_(data[bstack11111_opy_ (u"ࠬࡻࡲ࡭ࠩṴ")], bstack1l11lll1l11_opy_)
            bstack111l1111lll_opy_ = os.path.join(bstack1l11lll1l11_opy_, bstack1111l1ll111_opy_)
            os.chmod(bstack111l1111lll_opy_, 0o777) # bstack1111l111lll_opy_ permission
            return bstack111l1111lll_opy_
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨṵ").format(e))
    return binary_path
def bstack1111ll1111l_opy_(bstack1111l111l1l_opy_):
    try:
        if bstack11111_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭Ṷ") not in bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠨࡱࡶࠫṷ")].lower():
            return
        if os.path.exists(bstack11111_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṸ")):
            with open(bstack11111_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṹ"), bstack11111_opy_ (u"ࠦࡷࠨṺ")) as f:
                bstack1111lllll11_opy_ = {}
                for line in f:
                    if bstack11111_opy_ (u"ࠧࡃࠢṻ") in line:
                        key, value = line.rstrip().split(bstack11111_opy_ (u"ࠨ࠽ࠣṼ"), 1)
                        bstack1111lllll11_opy_[key] = value.strip(bstack11111_opy_ (u"ࠧࠣ࡞ࠪࠫṽ"))
                bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨṾ")] = bstack1111lllll11_opy_.get(bstack11111_opy_ (u"ࠤࡌࡈࠧṿ"), bstack11111_opy_ (u"ࠥࠦẀ"))
        elif os.path.exists(bstack11111_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡤࡰࡵ࡯࡮ࡦ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥẁ")):
            bstack1111l111l1l_opy_[bstack11111_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬẂ")] = bstack11111_opy_ (u"࠭ࡡ࡭ࡲ࡬ࡲࡪ࠭ẃ")
    except Exception as e:
        logger.debug(bstack11111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡥ࡫ࡶࡸࡷࡵࠠࡰࡨࠣࡰ࡮ࡴࡵࡹࠤẄ") + e)
@measure(event_name=EVENTS.bstack11l1l11l111_opy_, stage=STAGE.bstack111l1l11l_opy_)
def bstack1111l11111l_opy_(bstack111l11l1lll_opy_, bstack111l11l1l11_opy_):
    logger.debug(bstack11111_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥẅ") + str(bstack111l11l1lll_opy_) + bstack11111_opy_ (u"ࠤࠥẆ"))
    zip_path = os.path.join(bstack111l11l1l11_opy_, bstack11111_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤẇ"))
    bstack1111l1ll111_opy_ = bstack11111_opy_ (u"ࠫࠬẈ")
    with requests.get(bstack111l11l1lll_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11111_opy_ (u"ࠧࡽࡢࠣẉ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11111_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣẊ"))
    with zipfile.ZipFile(zip_path, bstack11111_opy_ (u"ࠧࡳࠩẋ")) as zip_ref:
        bstack1111l11ll11_opy_ = zip_ref.namelist()
        if len(bstack1111l11ll11_opy_) > 0:
            bstack1111l1ll111_opy_ = bstack1111l11ll11_opy_[0] # bstack1111l1lllll_opy_ bstack11l11l1l111_opy_ will be bstack1111llllll1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l11l1l11_opy_)
        logger.debug(bstack11111_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢẌ") + str(bstack111l11l1l11_opy_) + bstack11111_opy_ (u"ࠤࠪࠦẍ"))
    os.remove(zip_path)
    return bstack1111l1ll111_opy_
def get_cli_dir():
    bstack111l111ll11_opy_ = bstack1ll1l111l11_opy_()
    if bstack111l111ll11_opy_:
        bstack1l11lll1l11_opy_ = os.path.join(bstack111l111ll11_opy_, bstack11111_opy_ (u"ࠥࡧࡱ࡯ࠢẎ"))
        if not os.path.exists(bstack1l11lll1l11_opy_):
            os.makedirs(bstack1l11lll1l11_opy_, mode=0o777, exist_ok=True)
        return bstack1l11lll1l11_opy_
    else:
        raise FileNotFoundError(bstack11111_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢẏ"))
def bstack1l1l1l11ll1_opy_(bstack1l11lll1l11_opy_):
    bstack11111_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤẐ")
    bstack1111l11l1l1_opy_ = [
        os.path.join(bstack1l11lll1l11_opy_, f)
        for f in os.listdir(bstack1l11lll1l11_opy_)
        if os.path.isfile(os.path.join(bstack1l11lll1l11_opy_, f)) and f.startswith(bstack11111_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢẑ"))
    ]
    if len(bstack1111l11l1l1_opy_) > 0:
        return max(bstack1111l11l1l1_opy_, key=os.path.getmtime) # get bstack111l1ll111l_opy_ binary
    return bstack11111_opy_ (u"ࠢࠣẒ")
def bstack1111l1l1l11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1l1l1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1l1l1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11ll11l111_opy_(data, keys, default=None):
    bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡕࡤࡪࡪࡲࡹࠡࡩࡨࡸࠥࡧࠠ࡯ࡧࡶࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࠦࡦࡳࡱࡰࠤࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡥࡹࡧ࠺ࠡࡖ࡫ࡩࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶࠣࡸࡴࠦࡴࡳࡣࡹࡩࡷࡹࡥ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡫ࡦࡻࡶ࠾ࠥࡇࠠ࡭࡫ࡶࡸࠥࡵࡦࠡ࡭ࡨࡽࡸ࠵ࡩ࡯ࡦ࡬ࡧࡪࡹࠠࡳࡧࡳࡶࡪࡹࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡦࡨࡤࡹࡱࡺ࠺ࠡࡘࡤࡰࡺ࡫ࠠࡵࡱࠣࡶࡪࡺࡵࡳࡰࠣ࡭࡫ࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡶࡢ࡮ࡸࡩࠥࡧࡴࠡࡶ࡫ࡩࠥࡴࡥࡴࡶࡨࡨࠥࡶࡡࡵࡪ࠯ࠤࡴࡸࠠࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡩࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠋࠢࠣࠤࠥࠨࠢࠣẓ")
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