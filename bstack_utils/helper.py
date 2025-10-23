# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
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
from bstack_utils.constants import (bstack1l111ll11_opy_, bstack1ll1111111_opy_, bstack1l11111l1_opy_,
                                    bstack11l1l11ll1l_opy_, bstack11l1l111ll1_opy_, bstack11l11llllll_opy_, bstack11l11lll1l1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11lll1lll_opy_, bstack1l1ll1l1l_opy_
from bstack_utils.proxy import bstack1l111111ll_opy_, bstack1l1l1lllll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11111ll111_opy_
from bstack_utils.bstack1l1l11llll_opy_ import bstack11ll11l11_opy_
from browserstack_sdk._version import __version__
bstack11111lll_opy_ = Config.bstack111l111l_opy_()
logger = bstack11111ll111_opy_.get_logger(__name__, bstack11111ll111_opy_.bstack1l1l1lll11l_opy_())
def bstack1111ll1lll1_opy_(config):
    return config[bstack111111l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᯀ")]
def bstack111l1l1111l_opy_(config):
    return config[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᯁ")]
def bstack11lll111l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1l11ll1_opy_(obj):
    values = []
    bstack111l1ll1l1l_opy_ = re.compile(bstack111111l_opy_ (u"ࡳࠤࡡࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࡝ࡦ࠮ࠨࠧᯂ"), re.I)
    for key in obj.keys():
        if bstack111l1ll1l1l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111llll11l_opy_(config):
    tags = []
    tags.extend(bstack111l1l11ll1_opy_(os.environ))
    tags.extend(bstack111l1l11ll1_opy_(config))
    return tags
def bstack111l1111111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l111l1ll_opy_(bstack111l111lll1_opy_):
    if not bstack111l111lll1_opy_:
        return bstack111111l_opy_ (u"ࠩࠪᯃ")
    return bstack111111l_opy_ (u"ࠥࡿࢂࠦࠨࡼࡿࠬࠦᯄ").format(bstack111l111lll1_opy_.name, bstack111l111lll1_opy_.email)
def bstack111ll1111l1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l11ll1l1_opy_ = repo.common_dir
        info = {
            bstack111111l_opy_ (u"ࠦࡸ࡮ࡡࠣᯅ"): repo.head.commit.hexsha,
            bstack111111l_opy_ (u"ࠧࡹࡨࡰࡴࡷࡣࡸ࡮ࡡࠣᯆ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111111l_opy_ (u"ࠨࡢࡳࡣࡱࡧ࡭ࠨᯇ"): repo.active_branch.name,
            bstack111111l_opy_ (u"ࠢࡵࡣࡪࠦᯈ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࠦᯉ"): bstack111l111l1ll_opy_(repo.head.commit.committer),
            bstack111111l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࡤࡪࡡࡵࡧࠥᯊ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111111l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࠥᯋ"): bstack111l111l1ll_opy_(repo.head.commit.author),
            bstack111111l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡣࡩࡧࡴࡦࠤᯌ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111111l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᯍ"): repo.head.commit.message,
            bstack111111l_opy_ (u"ࠨࡲࡰࡱࡷࠦᯎ"): repo.git.rev_parse(bstack111111l_opy_ (u"ࠢ࠮࠯ࡶ࡬ࡴࡽ࠭ࡵࡱࡳࡰࡪࡼࡥ࡭ࠤᯏ")),
            bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲࡵ࡮ࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᯐ"): bstack111l11ll1l1_opy_,
            bstack111111l_opy_ (u"ࠤࡺࡳࡷࡱࡴࡳࡧࡨࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᯑ"): subprocess.check_output([bstack111111l_opy_ (u"ࠥ࡫࡮ࡺࠢᯒ"), bstack111111l_opy_ (u"ࠦࡷ࡫ࡶ࠮ࡲࡤࡶࡸ࡫ࠢᯓ"), bstack111111l_opy_ (u"ࠧ࠳࠭ࡨ࡫ࡷ࠱ࡨࡵ࡭࡮ࡱࡱ࠱ࡩ࡯ࡲࠣᯔ")]).strip().decode(
                bstack111111l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᯕ")),
            bstack111111l_opy_ (u"ࠢ࡭ࡣࡶࡸࡤࡺࡡࡨࠤᯖ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡴࡡࡶ࡭ࡳࡩࡥࡠ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᯗ"): repo.git.rev_list(
                bstack111111l_opy_ (u"ࠤࡾࢁ࠳࠴ࡻࡾࠤᯘ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111l1l11l1_opy_ = []
        for remote in remotes:
            bstack1111ll111ll_opy_ = {
                bstack111111l_opy_ (u"ࠥࡲࡦࡳࡥࠣᯙ"): remote.name,
                bstack111111l_opy_ (u"ࠦࡺࡸ࡬ࠣᯚ"): remote.url,
            }
            bstack1111l1l11l1_opy_.append(bstack1111ll111ll_opy_)
        bstack111l1l1l111_opy_ = {
            bstack111111l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᯛ"): bstack111111l_opy_ (u"ࠨࡧࡪࡶࠥᯜ"),
            **info,
            bstack111111l_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫ࡳࠣᯝ"): bstack1111l1l11l1_opy_
        }
        bstack111l1l1l111_opy_ = bstack111l1l1l1ll_opy_(bstack111l1l1l111_opy_)
        return bstack111l1l1l111_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᯞ").format(err))
        return {}
def bstack11lll111l11_opy_(bstack1111llll1ll_opy_=None):
    bstack111111l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡹࡰࡦࡥ࡬ࡪ࡮ࡩࡡ࡭࡮ࡼࠤ࡫ࡵࡲ࡮ࡣࡷࡸࡪࡪࠠࡧࡱࡵࠤࡆࡏࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡹࡸ࡫ࠠࡤࡣࡶࡩࡸࠦࡦࡰࡴࠣࡩࡦࡩࡨࠡࡨࡲࡰࡩ࡫ࡲࠡ࡫ࡱࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡫ࡵ࡬ࡥࡧࡵࡷࠥ࠮࡬ࡪࡵࡷ࠰ࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠩ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡪࡴࡲࡤࡦࡴࠣࡴࡦࡺࡨࡴࠢࡷࡳࠥ࡫ࡸࡵࡴࡤࡧࡹࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬ࡲࡰ࡯࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸࡸࠦࡴࡰࠢ࡞ࡳࡸ࠴ࡧࡦࡶࡦࡻࡩ࠮ࠩ࡞࠰ࠍࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡰ࡮ࡹࡴ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡨ࡮ࡩࡴࡴ࠮ࠣࡩࡦࡩࡨࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡣࠣࡪࡴࡲࡤࡦࡴ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᯟ")
    if bstack1111llll1ll_opy_ == None: # bstack111l11111l1_opy_ for bstack11lll11l1ll_opy_-repo
        bstack1111llll1ll_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111llll1ll_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack111111l_opy_ (u"ࠥࡴࡷࡏࡤࠣᯠ"): bstack111111l_opy_ (u"ࠦࠧᯡ"),
                bstack111111l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠦᯢ"): [],
                bstack111111l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢᯣ"): [],
                bstack111111l_opy_ (u"ࠢࡱࡴࡇࡥࡹ࡫ࠢᯤ"): bstack111111l_opy_ (u"ࠣࠤᯥ"),
                bstack111111l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡏࡨࡷࡸࡧࡧࡦࡵ᯦ࠥ"): [],
                bstack111111l_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᯧ"): bstack111111l_opy_ (u"ࠦࠧᯨ"),
                bstack111111l_opy_ (u"ࠧࡶࡲࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠧᯩ"): bstack111111l_opy_ (u"ࠨࠢᯪ"),
                bstack111111l_opy_ (u"ࠢࡱࡴࡕࡥࡼࡊࡩࡧࡨࠥᯫ"): bstack111111l_opy_ (u"ࠣࠤᯬ")
            }
            bstack111l1llll11_opy_ = repo.active_branch.name
            bstack1111l1lllll_opy_ = repo.head.commit
            result[bstack111111l_opy_ (u"ࠤࡳࡶࡎࡪࠢᯭ")] = bstack1111l1lllll_opy_.hexsha
            bstack1111ll1l1ll_opy_ = _111l111ll1l_opy_(repo)
            logger.debug(bstack111111l_opy_ (u"ࠥࡆࡦࡹࡥࠡࡤࡵࡥࡳࡩࡨࠡࡨࡲࡶࠥࡩ࡯࡮ࡲࡤࡶ࡮ࡹ࡯࡯࠼ࠣࠦᯮ") + str(bstack1111ll1l1ll_opy_) + bstack111111l_opy_ (u"ࠦࠧᯯ"))
            if bstack1111ll1l1ll_opy_:
                try:
                    bstack111l1l11l1l_opy_ = repo.git.diff(bstack111111l_opy_ (u"ࠧ࠳࠭࡯ࡣࡰࡩ࠲ࡵ࡮࡭ࡻࠥᯰ"), bstack1llll1ll1_opy_ (u"ࠨࡻࡣࡣࡶࡩࡤࡨࡲࡢࡰࡦ࡬ࢂ࠴࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦᯱ")).split(bstack111111l_opy_ (u"ࠧ࡝ࡰ᯲ࠪ"))
                    logger.debug(bstack111111l_opy_ (u"ࠣࡅ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾࠢࡤࡲࡩࠦࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾ࠼᯳ࠣࠦ") + str(bstack111l1l11l1l_opy_) + bstack111111l_opy_ (u"ࠤࠥ᯴"))
                    result[bstack111111l_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᯵")] = [f.strip() for f in bstack111l1l11l1l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1llll1ll1_opy_ (u"ࠦࢀࡨࡡࡴࡧࡢࡦࡷࡧ࡮ࡤࡪࢀ࠲࠳ࢁࡣࡶࡴࡵࡩࡳࡺ࡟ࡣࡴࡤࡲࡨ࡮ࡽࠣ᯶")))
                except Exception:
                    logger.debug(bstack111111l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡩࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡧ࡮ࡤࡪࠣࡧࡴࡳࡰࡢࡴ࡬ࡷࡴࡴ࠮ࠡࡈࡤࡰࡱ࡯࡮ࡨࠢࡥࡥࡨࡱࠠࡵࡱࠣࡶࡪࡩࡥ࡯ࡶࠣࡧࡴࡳ࡭ࡪࡶࡶ࠲ࠧ᯷"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack111111l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᯸")] = _1111ll1l11l_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack111111l_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᯹")] = _1111ll1l11l_opy_(commits[:5])
            bstack111l1ll11l1_opy_ = set()
            bstack111l11111ll_opy_ = []
            for commit in commits:
                logger.debug(bstack111111l_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡩ࡯࡮࡯࡬ࡸ࠿ࠦࠢ᯺") + str(commit.message) + bstack111111l_opy_ (u"ࠤࠥ᯻"))
                bstack111l1l1l11l_opy_ = commit.author.name if commit.author else bstack111111l_opy_ (u"࡙ࠥࡳࡱ࡮ࡰࡹࡱࠦ᯼")
                bstack111l1ll11l1_opy_.add(bstack111l1l1l11l_opy_)
                bstack111l11111ll_opy_.append({
                    bstack111111l_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧ᯽"): commit.message.strip(),
                    bstack111111l_opy_ (u"ࠧࡻࡳࡦࡴࠥ᯾"): bstack111l1l1l11l_opy_
                })
            result[bstack111111l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡹࠢ᯿")] = list(bstack111l1ll11l1_opy_)
            result[bstack111111l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡍࡦࡵࡶࡥ࡬࡫ࡳࠣᰀ")] = bstack111l11111ll_opy_
            result[bstack111111l_opy_ (u"ࠣࡲࡵࡈࡦࡺࡥࠣᰁ")] = bstack1111l1lllll_opy_.committed_datetime.strftime(bstack111111l_opy_ (u"ࠤࠨ࡝࠲ࠫ࡭࠮ࠧࡧࠦᰂ"))
            if (not result[bstack111111l_opy_ (u"ࠥࡴࡷ࡚ࡩࡵ࡮ࡨࠦᰃ")] or result[bstack111111l_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰄ")].strip() == bstack111111l_opy_ (u"ࠧࠨᰅ")) and bstack1111l1lllll_opy_.message:
                bstack111l11l1lll_opy_ = bstack1111l1lllll_opy_.message.strip().splitlines()
                result[bstack111111l_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰆ")] = bstack111l11l1lll_opy_[0] if bstack111l11l1lll_opy_ else bstack111111l_opy_ (u"ࠢࠣᰇ")
                if len(bstack111l11l1lll_opy_) > 2:
                    result[bstack111111l_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᰈ")] = bstack111111l_opy_ (u"ࠩ࡟ࡲࠬᰉ").join(bstack111l11l1lll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡄࡍࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࠪࡩࡳࡱࡪࡥࡳ࠼ࠣࡿ࡫ࡵ࡬ࡥࡧࡵࢁ࠮ࡀࠠࠣᰊ") + str(err) + bstack111111l_opy_ (u"ࠦࠧᰋ"))
    filtered_results = [
        result
        for result in results
        if _1111l1lll1l_opy_(result)
    ]
    return filtered_results
def _1111l1lll1l_opy_(result):
    bstack111111l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡥ࡭ࡲࡨࡶࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡪࡨࠣࡥࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡮ࡹࠠࡷࡣ࡯࡭ࡩࠦࠨ࡯ࡱࡱ࠱ࡪࡳࡰࡵࡻࠣࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠢࡤࡲࡩࠦࡡࡶࡶ࡫ࡳࡷࡹࠩ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰌ")
    return (
        isinstance(result.get(bstack111111l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰍ"), None), list)
        and len(result[bstack111111l_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᰎ")]) > 0
        and isinstance(result.get(bstack111111l_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡴࠤᰏ"), None), list)
        and len(result[bstack111111l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰐ")]) > 0
    )
def _111l111ll1l_opy_(repo):
    bstack111111l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡘࡷࡿࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡴࡩࡧࠣࡦࡦࡹࡥࠡࡤࡵࡥࡳࡩࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡴࡨࡴࡴࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡩࡣࡵࡨࡨࡵࡤࡦࡦࠣࡲࡦࡳࡥࡴࠢࡤࡲࡩࠦࡷࡰࡴ࡮ࠤࡼ࡯ࡴࡩࠢࡤࡰࡱࠦࡖࡄࡕࠣࡴࡷࡵࡶࡪࡦࡨࡶࡸ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣࡦࡷࡧ࡮ࡤࡪࠣ࡭࡫ࠦࡰࡰࡵࡶ࡭ࡧࡲࡥ࠭ࠢࡨࡰࡸ࡫ࠠࡏࡱࡱࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᰑ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111lll11ll_opy_ = origin.refs[bstack111111l_opy_ (u"ࠫࡍࡋࡁࡅࠩᰒ")]
            target = bstack1111lll11ll_opy_.reference.name
            if target.startswith(bstack111111l_opy_ (u"ࠬࡵࡲࡪࡩ࡬ࡲ࠴࠭ᰓ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack111111l_opy_ (u"࠭࡯ࡳ࡫ࡪ࡭ࡳ࠵ࠧᰔ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111ll1l11l_opy_(commits):
    bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡈࡧࡷࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡩࡨࡢࡰࡪࡩࡩࠦࡦࡪ࡮ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰕ")
    bstack111l1l11l1l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack1111ll11111_opy_ in diff:
                        if bstack1111ll11111_opy_.a_path:
                            bstack111l1l11l1l_opy_.add(bstack1111ll11111_opy_.a_path)
                        if bstack1111ll11111_opy_.b_path:
                            bstack111l1l11l1l_opy_.add(bstack1111ll11111_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l1l11l1l_opy_)
def bstack111l1l1l1ll_opy_(bstack111l1l1l111_opy_):
    bstack111l11l1l11_opy_ = bstack111l11ll111_opy_(bstack111l1l1l111_opy_)
    if bstack111l11l1l11_opy_ and bstack111l11l1l11_opy_ > bstack11l1l11ll1l_opy_:
        bstack111l111111l_opy_ = bstack111l11l1l11_opy_ - bstack11l1l11ll1l_opy_
        bstack1111lll1lll_opy_ = bstack111l1l1ll1l_opy_(bstack111l1l1l111_opy_[bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᰖ")], bstack111l111111l_opy_)
        bstack111l1l1l111_opy_[bstack111111l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᰗ")] = bstack1111lll1lll_opy_
        logger.info(bstack111111l_opy_ (u"ࠥࡘ࡭࡫ࠠࡤࡱࡰࡱ࡮ࡺࠠࡩࡣࡶࠤࡧ࡫ࡥ࡯ࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨ࠳ࠦࡓࡪࡼࡨࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࠠࡢࡨࡷࡩࡷࠦࡴࡳࡷࡱࡧࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡻࡾࠢࡎࡆࠧᰘ")
                    .format(bstack111l11ll111_opy_(bstack111l1l1l111_opy_) / 1024))
    return bstack111l1l1l111_opy_
def bstack111l11ll111_opy_(json_data):
    try:
        if json_data:
            bstack1111ll111l1_opy_ = json.dumps(json_data)
            bstack111l1ll1lll_opy_ = sys.getsizeof(bstack1111ll111l1_opy_)
            return bstack111l1ll1lll_opy_
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠦࡘࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡦࡲࡣࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡵ࡬ࡾࡪࠦ࡯ࡧࠢࡍࡗࡔࡔࠠࡰࡤ࡭ࡩࡨࡺ࠺ࠡࡽࢀࠦᰙ").format(e))
    return -1
def bstack111l1l1ll1l_opy_(field, bstack111ll111111_opy_):
    try:
        bstack1111l1l1l11_opy_ = len(bytes(bstack11l1l111ll1_opy_, bstack111111l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰚ")))
        bstack1111l1ll1l1_opy_ = bytes(field, bstack111111l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᰛ"))
        bstack1111l1ll11l_opy_ = len(bstack1111l1ll1l1_opy_)
        bstack1111llll1l1_opy_ = ceil(bstack1111l1ll11l_opy_ - bstack111ll111111_opy_ - bstack1111l1l1l11_opy_)
        if bstack1111llll1l1_opy_ > 0:
            bstack111l1lll1ll_opy_ = bstack1111l1ll1l1_opy_[:bstack1111llll1l1_opy_].decode(bstack111111l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᰜ"), errors=bstack111111l_opy_ (u"ࠨ࡫ࡪࡲࡴࡸࡥࠨᰝ")) + bstack11l1l111ll1_opy_
            return bstack111l1lll1ll_opy_
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡴࡸࡲࡨࡧࡴࡪࡰࡪࠤ࡫࡯ࡥ࡭ࡦ࠯ࠤࡳࡵࡴࡩ࡫ࡱ࡫ࠥࡽࡡࡴࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨࠥ࡮ࡥࡳࡧ࠽ࠤࢀࢃࠢᰞ").format(e))
    return field
def bstack111l11lll1_opy_():
    env = os.environ
    if (bstack111111l_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᰟ") in env and len(env[bstack111111l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤᰠ")]) > 0) or (
            bstack111111l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᰡ") in env and len(env[bstack111111l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧᰢ")]) > 0):
        return {
            bstack111111l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰣ"): bstack111111l_opy_ (u"ࠣࡌࡨࡲࡰ࡯࡮ࡴࠤᰤ"),
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᰥ"): env.get(bstack111111l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᰦ")),
            bstack111111l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᰧ"): env.get(bstack111111l_opy_ (u"ࠧࡐࡏࡃࡡࡑࡅࡒࡋࠢᰨ")),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᰩ"): env.get(bstack111111l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᰪ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠣࡅࡌࠦᰫ")) == bstack111111l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᰬ") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡆࡍࠧᰭ"))):
        return {
            bstack111111l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᰮ"): bstack111111l_opy_ (u"ࠧࡉࡩࡳࡥ࡯ࡩࡈࡏࠢᰯ"),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᰰ"): env.get(bstack111111l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᰱ")),
            bstack111111l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᰲ"): env.get(bstack111111l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡍࡓࡇࠨᰳ")),
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᰴ"): env.get(bstack111111l_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࠢᰵ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠧࡉࡉࠣᰶ")) == bstack111111l_opy_ (u"ࠨࡴࡳࡷࡨ᰷ࠦ") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙ࠢ᰸"))):
        return {
            bstack111111l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᰹"): bstack111111l_opy_ (u"ࠤࡗࡶࡦࡼࡩࡴࠢࡆࡍࠧ᰺"),
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᰻"): env.get(bstack111111l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢ࡛ࡊࡈ࡟ࡖࡔࡏࠦ᰼")),
            bstack111111l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᰽"): env.get(bstack111111l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ᰾")),
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᰿"): env.get(bstack111111l_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᱀"))
        }
    if env.get(bstack111111l_opy_ (u"ࠤࡆࡍࠧ᱁")) == bstack111111l_opy_ (u"ࠥࡸࡷࡻࡥࠣ᱂") and env.get(bstack111111l_opy_ (u"ࠦࡈࡏ࡟ࡏࡃࡐࡉࠧ᱃")) == bstack111111l_opy_ (u"ࠧࡩ࡯ࡥࡧࡶ࡬࡮ࡶࠢ᱄"):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᱅"): bstack111111l_opy_ (u"ࠢࡄࡱࡧࡩࡸ࡮ࡩࡱࠤ᱆"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᱇"): None,
            bstack111111l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᱈"): None,
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᱉"): None
        }
    if env.get(bstack111111l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡔࡄࡒࡈࡎࠢ᱊")) and env.get(bstack111111l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡅࡒࡑࡒࡏࡔࠣ᱋")):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᱌"): bstack111111l_opy_ (u"ࠢࡃ࡫ࡷࡦࡺࡩ࡫ࡦࡶࠥᱍ"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱎ"): env.get(bstack111111l_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡍࡉࡕࡡࡋࡘ࡙ࡖ࡟ࡐࡔࡌࡋࡎࡔࠢᱏ")),
            bstack111111l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᱐"): None,
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᱑"): env.get(bstack111111l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᱒"))
        }
    if env.get(bstack111111l_opy_ (u"ࠨࡃࡊࠤ᱓")) == bstack111111l_opy_ (u"ࠢࡵࡴࡸࡩࠧ᱔") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠣࡆࡕࡓࡓࡋࠢ᱕"))):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱖"): bstack111111l_opy_ (u"ࠥࡈࡷࡵ࡮ࡦࠤ᱗"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱘"): env.get(bstack111111l_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡐࡎࡔࡋࠣ᱙")),
            bstack111111l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱚ"): None,
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱛ"): env.get(bstack111111l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᱜ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠤࡆࡍࠧᱝ")) == bstack111111l_opy_ (u"ࠥࡸࡷࡻࡥࠣᱞ") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋࠢᱟ"))):
        return {
            bstack111111l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱠ"): bstack111111l_opy_ (u"ࠨࡓࡦ࡯ࡤࡴ࡭ࡵࡲࡦࠤᱡ"),
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱢ"): env.get(bstack111111l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡔࡘࡇࡂࡐࡌ࡞ࡆ࡚ࡉࡐࡐࡢ࡙ࡗࡒࠢᱣ")),
            bstack111111l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱤ"): env.get(bstack111111l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᱥ")),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱦ"): env.get(bstack111111l_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡏࡄࠣᱧ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠨࡃࡊࠤᱨ")) == bstack111111l_opy_ (u"ࠢࡵࡴࡸࡩࠧᱩ") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠣࡉࡌࡘࡑࡇࡂࡠࡅࡌࠦᱪ"))):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱫ"): bstack111111l_opy_ (u"ࠥࡋ࡮ࡺࡌࡢࡤࠥᱬ"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱭ"): env.get(bstack111111l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤ࡛ࡒࡍࠤᱮ")),
            bstack111111l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱯ"): env.get(bstack111111l_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᱰ")),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱱ"): env.get(bstack111111l_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡌࡈࠧᱲ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠥࡇࡎࠨᱳ")) == bstack111111l_opy_ (u"ࠦࡹࡸࡵࡦࠤᱴ") and bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࠣᱵ"))):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱶ"): bstack111111l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡱࡩࡵࡧࠥᱷ"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱸ"): env.get(bstack111111l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᱹ")),
            bstack111111l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱺ"): env.get(bstack111111l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡍࡃࡅࡉࡑࠨᱻ")) or env.get(bstack111111l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣᱼ")),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᱽ"): env.get(bstack111111l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᱾"))
        }
    if bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥ᱿"))):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲀ"): bstack111111l_opy_ (u"࡚ࠥ࡮ࡹࡵࡢ࡮ࠣࡗࡹࡻࡤࡪࡱࠣࡘࡪࡧ࡭ࠡࡕࡨࡶࡻ࡯ࡣࡦࡵࠥᲁ"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲂ"): bstack111111l_opy_ (u"ࠧࢁࡽࡼࡿࠥᲃ").format(env.get(bstack111111l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩᲄ")), env.get(bstack111111l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࡎࡊࠧᲅ"))),
            bstack111111l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲆ"): env.get(bstack111111l_opy_ (u"ࠤࡖ࡝ࡘ࡚ࡅࡎࡡࡇࡉࡋࡏࡎࡊࡖࡌࡓࡓࡏࡄࠣᲇ")),
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲈ"): env.get(bstack111111l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᲉ"))
        }
    if bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘࠢᲊ"))):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᲋"): bstack111111l_opy_ (u"ࠢࡂࡲࡳࡺࡪࡿ࡯ࡳࠤ᲌"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᲍"): bstack111111l_opy_ (u"ࠤࡾࢁ࠴ࡶࡲࡰ࡬ࡨࡧࡹ࠵ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠣ᲎").format(env.get(bstack111111l_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤ࡛ࡒࡍࠩ᲏")), env.get(bstack111111l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡁࡄࡅࡒ࡙ࡓ࡚࡟ࡏࡃࡐࡉࠬᲐ")), env.get(bstack111111l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡕࡏ࡙ࡌ࠭Ბ")), env.get(bstack111111l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪᲒ"))),
            bstack111111l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲓ"): env.get(bstack111111l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᲔ")),
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲕ"): env.get(bstack111111l_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᲖ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠦࡆࡠࡕࡓࡇࡢࡌ࡙࡚ࡐࡠࡗࡖࡉࡗࡥࡁࡈࡇࡑࡘࠧᲗ")) and env.get(bstack111111l_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢᲘ")):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲙ"): bstack111111l_opy_ (u"ࠢࡂࡼࡸࡶࡪࠦࡃࡊࠤᲚ"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲛ"): bstack111111l_opy_ (u"ࠤࡾࢁࢀࢃ࠯ࡠࡤࡸ࡭ࡱࡪ࠯ࡳࡧࡶࡹࡱࡺࡳࡀࡤࡸ࡭ࡱࡪࡉࡥ࠿ࡾࢁࠧᲜ").format(env.get(bstack111111l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭Ო")), env.get(bstack111111l_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࠩᲞ")), env.get(bstack111111l_opy_ (u"ࠬࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠬᲟ"))),
            bstack111111l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲠ"): env.get(bstack111111l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᲡ")),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲢ"): env.get(bstack111111l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᲣ"))
        }
    if any([env.get(bstack111111l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᲤ")), env.get(bstack111111l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡓࡇࡖࡓࡑ࡜ࡅࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥᲥ")), env.get(bstack111111l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᲦ"))]):
        return {
            bstack111111l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᲧ"): bstack111111l_opy_ (u"ࠢࡂ࡙ࡖࠤࡈࡵࡤࡦࡄࡸ࡭ࡱࡪࠢᲨ"),
            bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᲩ"): env.get(bstack111111l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡖࡕࡃࡎࡌࡇࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᲪ")),
            bstack111111l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲫ"): env.get(bstack111111l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᲬ")),
            bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲭ"): env.get(bstack111111l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᲮ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧᲯ")):
        return {
            bstack111111l_opy_ (u"ࠣࡰࡤࡱࡪࠨᲰ"): bstack111111l_opy_ (u"ࠤࡅࡥࡲࡨ࡯ࡰࠤᲱ"),
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲲ"): env.get(bstack111111l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡕࡩࡸࡻ࡬ࡵࡵࡘࡶࡱࠨᲳ")),
            bstack111111l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲴ"): env.get(bstack111111l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡳࡩࡱࡵࡸࡏࡵࡢࡏࡣࡰࡩࠧᲵ")),
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲶ"): env.get(bstack111111l_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨᲷ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࠥᲸ")) or env.get(bstack111111l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧᲹ")):
        return {
            bstack111111l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲺ"): bstack111111l_opy_ (u"ࠧ࡝ࡥࡳࡥ࡮ࡩࡷࠨ᲻"),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲼"): env.get(bstack111111l_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᲽ")),
            bstack111111l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲾ"): bstack111111l_opy_ (u"ࠤࡐࡥ࡮ࡴࠠࡑ࡫ࡳࡩࡱ࡯࡮ࡦࠤᲿ") if env.get(bstack111111l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡒࡇࡉࡏࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡘ࡚ࡁࡓࡖࡈࡈࠧ᳀")) else None,
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᳁"): env.get(bstack111111l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡇࡊࡖࡢࡇࡔࡓࡍࡊࡖࠥ᳂"))
        }
    if any([env.get(bstack111111l_opy_ (u"ࠨࡇࡄࡒࡢࡔࡗࡕࡊࡆࡅࡗࠦ᳃")), env.get(bstack111111l_opy_ (u"ࠢࡈࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣ᳄")), env.get(bstack111111l_opy_ (u"ࠣࡉࡒࡓࡌࡒࡅࡠࡅࡏࡓ࡚ࡊ࡟ࡑࡔࡒࡎࡊࡉࡔࠣ᳅"))]):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳆"): bstack111111l_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡇࡱࡵࡵࡥࠤ᳇"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᳈"): None,
            bstack111111l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳉"): env.get(bstack111111l_opy_ (u"ࠨࡐࡓࡑࡍࡉࡈ࡚࡟ࡊࡆࠥ᳊")),
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳋"): env.get(bstack111111l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ᳌"))
        }
    if env.get(bstack111111l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࠧ᳍")):
        return {
            bstack111111l_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳎"): bstack111111l_opy_ (u"ࠦࡘ࡮ࡩࡱࡲࡤࡦࡱ࡫ࠢ᳏"),
            bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᳐"): env.get(bstack111111l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧ᳑")),
            bstack111111l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳒"): bstack111111l_opy_ (u"ࠣࡌࡲࡦࠥࠩࡻࡾࠤ᳓").format(env.get(bstack111111l_opy_ (u"ࠩࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈ᳔ࠬ"))) if env.get(bstack111111l_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉࠨ᳕")) else None,
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳖ࠥ"): env.get(bstack111111l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘ᳗ࠢ"))
        }
    if bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠨࡎࡆࡖࡏࡍࡋ࡟᳘ࠢ"))):
        return {
            bstack111111l_opy_ (u"ࠢ࡯ࡣࡰࡩ᳙ࠧ"): bstack111111l_opy_ (u"ࠣࡐࡨࡸࡱ࡯ࡦࡺࠤ᳚"),
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳛"): env.get(bstack111111l_opy_ (u"ࠥࡈࡊࡖࡌࡐ࡛ࡢ࡙ࡗࡒ᳜ࠢ")),
            bstack111111l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳝"): env.get(bstack111111l_opy_ (u"࡙ࠧࡉࡕࡇࡢࡒࡆࡓࡅ᳞ࠣ")),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳟ࠧ"): env.get(bstack111111l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳠"))
        }
    if bstack1llll11lll_opy_(env.get(bstack111111l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡃࡆࡘࡎࡕࡎࡔࠤ᳡"))):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫᳢ࠢ"): bstack111111l_opy_ (u"ࠥࡋ࡮ࡺࡈࡶࡤࠣࡅࡨࡺࡩࡰࡰࡶ᳣ࠦ"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳤ࠢ"): bstack111111l_opy_ (u"ࠧࢁࡽ࠰ࡽࢀ࠳ࡦࡩࡴࡪࡱࡱࡷ࠴ࡸࡵ࡯ࡵ࠲ࡿࢂࠨ᳥").format(env.get(bstack111111l_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡓࡆࡔ࡙ࡉࡗࡥࡕࡓࡎ᳦ࠪ")), env.get(bstack111111l_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡇࡓࡓࡘࡏࡔࡐࡔ࡜᳧ࠫ")), env.get(bstack111111l_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠨ᳨"))),
            bstack111111l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᳩ"): env.get(bstack111111l_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢ࡛ࡔࡘࡋࡇࡎࡒ࡛ࠧᳪ")),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᳫ"): env.get(bstack111111l_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠧᳬ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠨࡃࡊࠤ᳭")) == bstack111111l_opy_ (u"ࠢࡵࡴࡸࡩࠧᳮ") and env.get(bstack111111l_opy_ (u"ࠣࡘࡈࡖࡈࡋࡌࠣᳯ")) == bstack111111l_opy_ (u"ࠤ࠴ࠦᳰ"):
        return {
            bstack111111l_opy_ (u"ࠥࡲࡦࡳࡥࠣᳱ"): bstack111111l_opy_ (u"࡛ࠦ࡫ࡲࡤࡧ࡯ࠦᳲ"),
            bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᳳ"): bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࡻࡾࠤ᳴").format(env.get(bstack111111l_opy_ (u"ࠧࡗࡇࡕࡇࡊࡒ࡟ࡖࡔࡏࠫᳵ"))),
            bstack111111l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᳶ"): None,
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳷"): None,
        }
    if env.get(bstack111111l_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ᳸")):
        return {
            bstack111111l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳹"): bstack111111l_opy_ (u"࡚ࠧࡥࡢ࡯ࡦ࡭ࡹࡿࠢᳺ"),
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳻"): None,
            bstack111111l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳼"): env.get(bstack111111l_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢࡔࡗࡕࡊࡆࡅࡗࡣࡓࡇࡍࡆࠤ᳽")),
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳾"): env.get(bstack111111l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᳿"))
        }
    if any([env.get(bstack111111l_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋࠢᴀ")), env.get(bstack111111l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡕࡐࠧᴁ")), env.get(bstack111111l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡗࡊࡘࡎࡂࡏࡈࠦᴂ")), env.get(bstack111111l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢࡘࡊࡇࡍࠣᴃ"))]):
        return {
            bstack111111l_opy_ (u"ࠣࡰࡤࡱࡪࠨᴄ"): bstack111111l_opy_ (u"ࠤࡆࡳࡳࡩ࡯ࡶࡴࡶࡩࠧᴅ"),
            bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴆ"): None,
            bstack111111l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴇ"): env.get(bstack111111l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᴈ")) or None,
            bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴉ"): env.get(bstack111111l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᴊ"), 0)
        }
    if env.get(bstack111111l_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᴋ")):
        return {
            bstack111111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴌ"): bstack111111l_opy_ (u"ࠥࡋࡴࡉࡄࠣᴍ"),
            bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴎ"): None,
            bstack111111l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴏ"): env.get(bstack111111l_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᴐ")),
            bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴑ"): env.get(bstack111111l_opy_ (u"ࠣࡉࡒࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡃࡐࡗࡑࡘࡊࡘࠢᴒ"))
        }
    if env.get(bstack111111l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᴓ")):
        return {
            bstack111111l_opy_ (u"ࠥࡲࡦࡳࡥࠣᴔ"): bstack111111l_opy_ (u"ࠦࡈࡵࡤࡦࡈࡵࡩࡸ࡮ࠢᴕ"),
            bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴖ"): env.get(bstack111111l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᴗ")),
            bstack111111l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴘ"): env.get(bstack111111l_opy_ (u"ࠣࡅࡉࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᴙ")),
            bstack111111l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴚ"): env.get(bstack111111l_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᴛ"))
        }
    return {bstack111111l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴜ"): None}
def get_host_info():
    return {
        bstack111111l_opy_ (u"ࠧ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠢᴝ"): platform.node(),
        bstack111111l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣᴞ"): platform.system(),
        bstack111111l_opy_ (u"ࠢࡵࡻࡳࡩࠧᴟ"): platform.machine(),
        bstack111111l_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤᴠ"): platform.version(),
        bstack111111l_opy_ (u"ࠤࡤࡶࡨ࡮ࠢᴡ"): platform.architecture()[0]
    }
def bstack11ll1l1lll_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1111l1l_opy_():
    if bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫᴢ")):
        return bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᴣ")
    return bstack111111l_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠫᴤ")
def bstack111l1l1ll11_opy_(driver):
    info = {
        bstack111111l_opy_ (u"࠭ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᴥ"): driver.capabilities,
        bstack111111l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫᴦ"): driver.session_id,
        bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩᴧ"): driver.capabilities.get(bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᴨ"), None),
        bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᴩ"): driver.capabilities.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᴪ"), None),
        bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࠧᴫ"): driver.capabilities.get(bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬᴬ"), None),
        bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪᴭ"):driver.capabilities.get(bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪᴮ"), None),
    }
    if bstack111l1111l1l_opy_() == bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᴯ"):
        if bstack11l11lll1l_opy_():
            info[bstack111111l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᴰ")] = bstack111111l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪᴱ")
        elif driver.capabilities.get(bstack111111l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᴲ"), {}).get(bstack111111l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᴳ"), False):
            info[bstack111111l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨᴴ")] = bstack111111l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᴵ")
        else:
            info[bstack111111l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᴶ")] = bstack111111l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᴷ")
    return info
def bstack11l11lll1l_opy_():
    if bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪᴸ")):
        return True
    if bstack1llll11lll_opy_(os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ᴹ"), None)):
        return True
    return False
def bstack1l11l1ll1l_opy_(bstack1111llll111_opy_, url, data, config):
    headers = config.get(bstack111111l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᴺ"), None)
    proxies = bstack1l111111ll_opy_(config, url)
    auth = config.get(bstack111111l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᴻ"), None)
    response = requests.request(
            bstack1111llll111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1ll1l1l1_opy_(bstack11lll111ll_opy_, size):
    bstack11l1ll1l1l_opy_ = []
    while len(bstack11lll111ll_opy_) > size:
        bstack1lll111ll1_opy_ = bstack11lll111ll_opy_[:size]
        bstack11l1ll1l1l_opy_.append(bstack1lll111ll1_opy_)
        bstack11lll111ll_opy_ = bstack11lll111ll_opy_[size:]
    bstack11l1ll1l1l_opy_.append(bstack11lll111ll_opy_)
    return bstack11l1ll1l1l_opy_
def bstack111l1111ll1_opy_(message, bstack111l11l1ll1_opy_=False):
    os.write(1, bytes(message, bstack111111l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᴼ")))
    os.write(1, bytes(bstack111111l_opy_ (u"ࠩ࡟ࡲࠬᴽ"), bstack111111l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᴾ")))
    if bstack111l11l1ll1_opy_:
        with open(bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡴ࠷࠱ࡺ࠯ࠪᴿ") + os.environ[bstack111111l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᵀ")] + bstack111111l_opy_ (u"࠭࠮࡭ࡱࡪࠫᵁ"), bstack111111l_opy_ (u"ࠧࡢࠩᵂ")) as f:
            f.write(message + bstack111111l_opy_ (u"ࠨ࡞ࡱࠫᵃ"))
def bstack1lll1ll1l1l_opy_():
    return os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᵄ")].lower() == bstack111111l_opy_ (u"ࠪࡸࡷࡻࡥࠨᵅ")
def bstack1llll1ll_opy_():
    return bstack1llll11l_opy_().replace(tzinfo=None).isoformat() + bstack111111l_opy_ (u"ࠫ࡟࠭ᵆ")
def bstack111l1ll11ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111111l_opy_ (u"ࠬࡠࠧᵇ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111111l_opy_ (u"࡚࠭ࠨᵈ")))).total_seconds() * 1000
def bstack1111l1ll111_opy_(timestamp):
    return bstack1111l1l111l_opy_(timestamp).isoformat() + bstack111111l_opy_ (u"࡛ࠧࠩᵉ")
def bstack111l11l1111_opy_(bstack111l1ll1111_opy_):
    date_format = bstack111111l_opy_ (u"ࠨࠧ࡜ࠩࡲࠫࡤࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫࠭ᵊ")
    bstack111l111ll11_opy_ = datetime.datetime.strptime(bstack111l1ll1111_opy_, date_format)
    return bstack111l111ll11_opy_.isoformat() + bstack111111l_opy_ (u"ࠩ࡝ࠫᵋ")
def bstack1111ll11ll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᵌ")
    else:
        return bstack111111l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᵍ")
def bstack1llll11lll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111111l_opy_ (u"ࠬࡺࡲࡶࡧࠪᵎ")
def bstack111l111l111_opy_(val):
    return val.__str__().lower() == bstack111111l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬᵏ")
def error_handler(bstack1111lll1ll1_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111lll1ll1_opy_ as e:
                print(bstack111111l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢᵐ").format(func.__name__, bstack1111lll1ll1_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll1111l_opy_(bstack1111ll1llll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111ll1llll_opy_(cls, *args, **kwargs)
            except bstack1111lll1ll1_opy_ as e:
                print(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣᵑ").format(bstack1111ll1llll_opy_.__name__, bstack1111lll1ll1_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll1111l_opy_
    else:
        return decorator
def bstack11l1l1l1ll_opy_(bstack111l11ll_opy_):
    if os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬᵒ")) is not None:
        return bstack1llll11lll_opy_(os.getenv(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᵓ")))
    if bstack111111l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵔ") in bstack111l11ll_opy_ and bstack111l111l111_opy_(bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᵕ")]):
        return False
    if bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᵖ") in bstack111l11ll_opy_ and bstack111l111l111_opy_(bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᵗ")]):
        return False
    return True
def bstack1ll11111l1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111ll1111ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠣᵘ"), None)
        return bstack111ll1111ll_opy_ is None or bstack111ll1111ll_opy_ == bstack111111l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᵙ")
    except Exception as e:
        return False
def bstack11l1l11ll1_opy_(hub_url, CONFIG):
    if bstack1ll1llllll_opy_() <= version.parse(bstack111111l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪᵚ")):
        if hub_url:
            return bstack111111l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᵛ") + hub_url + bstack111111l_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤᵜ")
        return bstack1ll1111111_opy_
    if hub_url:
        return bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᵝ") + hub_url + bstack111111l_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣᵞ")
    return bstack1l11111l1_opy_
def bstack1111ll11l11_opy_():
    return isinstance(os.getenv(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧᵟ")), str)
def bstack111ll11l1l_opy_(url):
    return urlparse(url).hostname
def bstack111lll11l1_opy_(hostname):
    for bstack1ll1l111ll_opy_ in bstack1l111ll11_opy_:
        regex = re.compile(bstack1ll1l111ll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111lll1_opy_(bstack111l11ll1ll_opy_, file_name, logger):
    bstack1111l11l11_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠩࢁࠫᵠ")), bstack111l11ll1ll_opy_)
    try:
        if not os.path.exists(bstack1111l11l11_opy_):
            os.makedirs(bstack1111l11l11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠪࢂࠬᵡ")), bstack111l11ll1ll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111111l_opy_ (u"ࠫࡼ࠭ᵢ")):
                pass
            with open(file_path, bstack111111l_opy_ (u"ࠧࡽࠫࠣᵣ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11lll1lll_opy_.format(str(e)))
def bstack11ll11l111l_opy_(file_name, key, value, logger):
    file_path = bstack11ll111lll1_opy_(bstack111111l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᵤ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1111l1lll1_opy_ = json.load(open(file_path, bstack111111l_opy_ (u"ࠧࡳࡤࠪᵥ")))
        else:
            bstack1111l1lll1_opy_ = {}
        bstack1111l1lll1_opy_[key] = value
        with open(file_path, bstack111111l_opy_ (u"ࠣࡹ࠮ࠦᵦ")) as outfile:
            json.dump(bstack1111l1lll1_opy_, outfile)
def bstack1ll1l1ll1_opy_(file_name, logger):
    file_path = bstack11ll111lll1_opy_(bstack111111l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵧ"), file_name, logger)
    bstack1111l1lll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111111l_opy_ (u"ࠪࡶࠬᵨ")) as bstack1l1ll1l111_opy_:
            bstack1111l1lll1_opy_ = json.load(bstack1l1ll1l111_opy_)
    return bstack1111l1lll1_opy_
def bstack11l1lll11l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡨ࡬ࡰࡪࡀࠠࠨᵩ") + file_path + bstack111111l_opy_ (u"ࠬࠦࠧᵪ") + str(e))
def bstack1ll1llllll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111111l_opy_ (u"ࠨ࠼ࡏࡑࡗࡗࡊ࡚࠾ࠣᵫ")
def bstack111ll11lll_opy_(config):
    if bstack111111l_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᵬ") in config:
        del (config[bstack111111l_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᵭ")])
        return False
    if bstack1ll1llllll_opy_() < version.parse(bstack111111l_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨᵮ")):
        return False
    if bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠪ࠸࠳࠷࠮࠶ࠩᵯ")):
        return True
    if bstack111111l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᵰ") in config and config[bstack111111l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᵱ")] is False:
        return False
    else:
        return True
def bstack1l1lll1111_opy_(args_list, bstack111l11l11l1_opy_):
    index = -1
    for value in bstack111l11l11l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111lll11l1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111lll11l1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll111_opy_ = bstack1llll111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111111l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᵲ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᵳ"), exception=exception)
    def bstack11111l111l_opy_(self):
        if self.result != bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵴ"):
            return None
        if isinstance(self.exception_type, str) and bstack111111l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧᵵ") in self.exception_type:
            return bstack111111l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᵶ")
        return bstack111111l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᵷ")
    def bstack111ll111l11_opy_(self):
        if self.result != bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᵸ"):
            return None
        if self.bstack1llll111_opy_:
            return self.bstack1llll111_opy_
        return bstack111l111l11l_opy_(self.exception)
def bstack111l111l11l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1111l11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1lll111l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll1ll1ll1_opy_(config, logger):
    try:
        import playwright
        bstack1111l1l1l1l_opy_ = playwright.__file__
        bstack111l1ll1l11_opy_ = os.path.split(bstack1111l1l1l1l_opy_)
        bstack1111l1l1ll1_opy_ = bstack111l1ll1l11_opy_[0] + bstack111111l_opy_ (u"࠭࠯ࡥࡴ࡬ࡺࡪࡸ࠯ࡱࡣࡦ࡯ࡦ࡭ࡥ࠰࡮࡬ࡦ࠴ࡩ࡬ࡪ࠱ࡦࡰ࡮࠴ࡪࡴࠩᵹ")
        os.environ[bstack111111l_opy_ (u"ࠧࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠪᵺ")] = bstack1l1l1lllll_opy_(config)
        with open(bstack1111l1l1ll1_opy_, bstack111111l_opy_ (u"ࠨࡴࠪᵻ")) as f:
            file_content = f.read()
            bstack111l1l1l1l1_opy_ = bstack111111l_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨᵼ")
            bstack111l1l11lll_opy_ = file_content.find(bstack111l1l1l1l1_opy_)
            if bstack111l1l11lll_opy_ == -1:
              process = subprocess.Popen(bstack111111l_opy_ (u"ࠥࡲࡵࡳࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠢᵽ"), shell=True, cwd=bstack111l1ll1l11_opy_[0])
              process.wait()
              bstack111l1l11l11_opy_ = bstack111111l_opy_ (u"ࠫࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵࠤ࠾ࠫᵾ")
              bstack111l1111lll_opy_ = bstack111111l_opy_ (u"ࠧࠨࠢࠡ࡞ࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺ࡜ࠣ࠽ࠣࡧࡴࡴࡳࡵࠢࡾࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠠࡾࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬ࠯࠻ࠡ࡫ࡩࠤ࠭ࡶࡲࡰࡥࡨࡷࡸ࠴ࡥ࡯ࡸ࠱ࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠯ࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠫ࠭ࡀࠦࠢࠣࠤᵿ")
              bstack111l11l111l_opy_ = file_content.replace(bstack111l1l11l11_opy_, bstack111l1111lll_opy_)
              with open(bstack1111l1l1ll1_opy_, bstack111111l_opy_ (u"࠭ࡷࠨᶀ")) as f:
                f.write(bstack111l11l111l_opy_)
    except Exception as e:
        logger.error(bstack1l1ll1l1l_opy_.format(str(e)))
def bstack11l1ll11ll_opy_():
  try:
    bstack111l1l111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭࠰࡭ࡷࡴࡴࠧᶁ"))
    bstack111l11ll11l_opy_ = []
    if os.path.exists(bstack111l1l111ll_opy_):
      with open(bstack111l1l111ll_opy_) as f:
        bstack111l11ll11l_opy_ = json.load(f)
      os.remove(bstack111l1l111ll_opy_)
    return bstack111l11ll11l_opy_
  except:
    pass
  return []
def bstack111ll11l1_opy_(bstack11l111l1ll_opy_):
  try:
    bstack111l11ll11l_opy_ = []
    bstack111l1l111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᶂ"))
    if os.path.exists(bstack111l1l111ll_opy_):
      with open(bstack111l1l111ll_opy_) as f:
        bstack111l11ll11l_opy_ = json.load(f)
    bstack111l11ll11l_opy_.append(bstack11l111l1ll_opy_)
    with open(bstack111l1l111ll_opy_, bstack111111l_opy_ (u"ࠩࡺࠫᶃ")) as f:
        json.dump(bstack111l11ll11l_opy_, f)
  except:
    pass
def bstack1l111ll1l_opy_(logger, bstack111l1lll1l1_opy_ = False):
  try:
    test_name = os.environ.get(bstack111111l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭ᶄ"), bstack111111l_opy_ (u"ࠫࠬᶅ"))
    if test_name == bstack111111l_opy_ (u"ࠬ࠭ᶆ"):
        test_name = threading.current_thread().__dict__.get(bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡈࡤࡥࡡࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠬᶇ"), bstack111111l_opy_ (u"ࠧࠨᶈ"))
    bstack1111l1llll1_opy_ = bstack111111l_opy_ (u"ࠨ࠮ࠣࠫᶉ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1lll1l1_opy_:
        bstack1111ll111l_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᶊ"), bstack111111l_opy_ (u"ࠪ࠴ࠬᶋ"))
        bstack11l11lllll_opy_ = {bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶌ"): test_name, bstack111111l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶍ"): bstack1111l1llll1_opy_, bstack111111l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶎ"): bstack1111ll111l_opy_}
        bstack111l11llll1_opy_ = []
        bstack111l1lllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᶏ"))
        if os.path.exists(bstack111l1lllll1_opy_):
            with open(bstack111l1lllll1_opy_) as f:
                bstack111l11llll1_opy_ = json.load(f)
        bstack111l11llll1_opy_.append(bstack11l11lllll_opy_)
        with open(bstack111l1lllll1_opy_, bstack111111l_opy_ (u"ࠨࡹࠪᶐ")) as f:
            json.dump(bstack111l11llll1_opy_, f)
    else:
        bstack11l11lllll_opy_ = {bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᶑ"): test_name, bstack111111l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᶒ"): bstack1111l1llll1_opy_, bstack111111l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᶓ"): str(multiprocessing.current_process().name)}
        if bstack111111l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩᶔ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11l11lllll_opy_)
  except Exception as e:
      logger.warn(bstack111111l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡲࡼࡸࡪࡹࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᶕ").format(e))
def bstack1l11ll1ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪᶖ"))
    try:
      bstack1111l1lll11_opy_ = []
      bstack11l11lllll_opy_ = {bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶗ"): test_name, bstack111111l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶘ"): error_message, bstack111111l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶙ"): index}
      bstack111l111llll_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᶚ"))
      if os.path.exists(bstack111l111llll_opy_):
          with open(bstack111l111llll_opy_) as f:
              bstack1111l1lll11_opy_ = json.load(f)
      bstack1111l1lll11_opy_.append(bstack11l11lllll_opy_)
      with open(bstack111l111llll_opy_, bstack111111l_opy_ (u"ࠬࡽࠧᶛ")) as f:
          json.dump(bstack1111l1lll11_opy_, f)
    except Exception as e:
      logger.warn(bstack111111l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡴࡲࡦࡴࡺࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᶜ").format(e))
    return
  bstack1111l1lll11_opy_ = []
  bstack11l11lllll_opy_ = {bstack111111l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶝ"): test_name, bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶞ"): error_message, bstack111111l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶟ"): index}
  bstack111l111llll_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫᶠ"))
  lock_file = bstack111l111llll_opy_ + bstack111111l_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪᶡ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l111llll_opy_):
          with open(bstack111l111llll_opy_, bstack111111l_opy_ (u"ࠬࡸࠧᶢ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111l1lll11_opy_ = json.load(open(bstack111l111llll_opy_))
      bstack1111l1lll11_opy_.append(bstack11l11lllll_opy_)
      with open(bstack111l111llll_opy_, bstack111111l_opy_ (u"࠭ࡷࠨᶣ")) as f:
          json.dump(bstack1111l1lll11_opy_, f)
  except Exception as e:
    logger.warn(bstack111111l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩ࠽ࠤࢀࢃࠢᶤ").format(e))
def bstack1ll1l1ll1l_opy_(bstack111l1ll1ll_opy_, name, logger):
  try:
    bstack11l11lllll_opy_ = {bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᶥ"): name, bstack111111l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᶦ"): bstack111l1ll1ll_opy_, bstack111111l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᶧ"): str(threading.current_thread()._name)}
    return bstack11l11lllll_opy_
  except Exception as e:
    logger.warn(bstack111111l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡢࡦࡪࡤࡺࡪࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᶨ").format(e))
  return
def bstack111l111l1l1_opy_():
    return platform.system() == bstack111111l_opy_ (u"ࠬ࡝ࡩ࡯ࡦࡲࡻࡸ࠭ᶩ")
def bstack1l1lll1l11_opy_(bstack111l11l11ll_opy_, config, logger):
    bstack1111ll11lll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l11l11ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡱࡺࡥࡳࠢࡦࡳࡳ࡬ࡩࡨࠢ࡮ࡩࡾࡹࠠࡣࡻࠣࡶࡪ࡭ࡥࡹࠢࡰࡥࡹࡩࡨ࠻ࠢࡾࢁࠧᶪ").format(e))
    return bstack1111ll11lll_opy_
def bstack11l1ll11l1l_opy_(bstack111l1l11111_opy_, bstack1111lll1111_opy_):
    bstack111l1l111l1_opy_ = version.parse(bstack111l1l11111_opy_)
    bstack1111lll1l1l_opy_ = version.parse(bstack1111lll1111_opy_)
    if bstack111l1l111l1_opy_ > bstack1111lll1l1l_opy_:
        return 1
    elif bstack111l1l111l1_opy_ < bstack1111lll1l1l_opy_:
        return -1
    else:
        return 0
def bstack1llll11l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l1l111l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1llll1l_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1l111l1l1l_opy_(options, framework, config, bstack1l1l1l1ll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack111111l_opy_ (u"ࠧࡨࡧࡷࠫᶫ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1lllll111l_opy_ = caps.get(bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᶬ"))
    bstack1111lll111l_opy_ = True
    bstack11ll1lll1_opy_ = os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᶭ")]
    bstack1l1111l1lll_opy_ = config.get(bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᶮ"), False)
    if bstack1l1111l1lll_opy_:
        bstack1l1l1ll1l11_opy_ = config.get(bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᶯ"), {})
        bstack1l1l1ll1l11_opy_[bstack111111l_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨᶰ")] = os.getenv(bstack111111l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᶱ"))
        bstack111l1ll1ll1_opy_ = json.loads(os.getenv(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᶲ"), bstack111111l_opy_ (u"ࠨࡽࢀࠫᶳ"))).get(bstack111111l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᶴ"))
    if bstack111l111l111_opy_(caps.get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪ࡝࠳ࡄࠩᶵ"))) or bstack111l111l111_opy_(caps.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫᶶ"))):
        bstack1111lll111l_opy_ = False
    if bstack111ll11lll_opy_({bstack111111l_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧᶷ"): bstack1111lll111l_opy_}):
        bstack1lllll111l_opy_ = bstack1lllll111l_opy_ or {}
        bstack1lllll111l_opy_[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᶸ")] = bstack111l1llll1l_opy_(framework)
        bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶹ")] = bstack1lll1ll1l1l_opy_()
        bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᶺ")] = bstack11ll1lll1_opy_
        bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᶻ")] = bstack1l1l1l1ll_opy_
        if bstack1l1111l1lll_opy_:
            bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᶼ")] = bstack1l1111l1lll_opy_
            bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᶽ")] = bstack1l1l1ll1l11_opy_
            bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᶾ")][bstack111111l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᶿ")] = bstack111l1ll1ll1_opy_
        if getattr(options, bstack111111l_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᷀"), None):
            options.set_capability(bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᷁"), bstack1lllll111l_opy_)
        else:
            options[bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵ᷂ࠪ")] = bstack1lllll111l_opy_
    else:
        if getattr(options, bstack111111l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫ᷃"), None):
            options.set_capability(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ᷄"), bstack111l1llll1l_opy_(framework))
            options.set_capability(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᷅"), bstack1lll1ll1l1l_opy_())
            options.set_capability(bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᷆"), bstack11ll1lll1_opy_)
            options.set_capability(bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ᷇"), bstack1l1l1l1ll_opy_)
            if bstack1l1111l1lll_opy_:
                options.set_capability(bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ᷈"), bstack1l1111l1lll_opy_)
                options.set_capability(bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᷉"), bstack1l1l1ll1l11_opy_)
                options.set_capability(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴ࠰ࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰ᷊ࠪ"), bstack111l1ll1ll1_opy_)
        else:
            options[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ᷋")] = bstack111l1llll1l_opy_(framework)
            options[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭᷌")] = bstack1lll1ll1l1l_opy_()
            options[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ᷍")] = bstack11ll1lll1_opy_
            options[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ᷎")] = bstack1l1l1l1ll_opy_
            if bstack1l1111l1lll_opy_:
                options[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ᷏ࠧ")] = bstack1l1111l1lll_opy_
                options[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᷐")] = bstack1l1l1ll1l11_opy_
                options[bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᷑")][bstack111111l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᷒")] = bstack111l1ll1ll1_opy_
    return options
def bstack111l1lll11l_opy_(ws_endpoint, framework):
    bstack1l1l1l1ll_opy_ = bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢᷓ"))
    if ws_endpoint and len(ws_endpoint.split(bstack111111l_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬᷔ"))) > 1:
        ws_url = ws_endpoint.split(bstack111111l_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭ᷕ"))[0]
        if bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫᷖ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l11lll11_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack111111l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᷗ"))[1]))
            bstack111l11lll11_opy_ = bstack111l11lll11_opy_ or {}
            bstack11ll1lll1_opy_ = os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᷘ")]
            bstack111l11lll11_opy_[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᷙ")] = str(framework) + str(__version__)
            bstack111l11lll11_opy_[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᷚ")] = bstack1lll1ll1l1l_opy_()
            bstack111l11lll11_opy_[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᷛ")] = bstack11ll1lll1_opy_
            bstack111l11lll11_opy_[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᷜ")] = bstack1l1l1l1ll_opy_
            ws_endpoint = ws_endpoint.split(bstack111111l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧᷝ"))[0] + bstack111111l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᷞ") + urllib.parse.quote(json.dumps(bstack111l11lll11_opy_))
    return ws_endpoint
def bstack111ll1lll1_opy_():
    global bstack1111lllll1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1111lllll1_opy_ = BrowserType.connect
    return bstack1111lllll1_opy_
def bstack111lll1111_opy_(framework_name):
    global bstack1l111111l_opy_
    bstack1l111111l_opy_ = framework_name
    return framework_name
def bstack1l1l1lll1l_opy_(self, *args, **kwargs):
    global bstack1111lllll1_opy_
    try:
        global bstack1l111111l_opy_
        if bstack111111l_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧᷟ") in kwargs:
            kwargs[bstack111111l_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨᷠ")] = bstack111l1lll11l_opy_(
                kwargs.get(bstack111111l_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩᷡ"), None),
                bstack1l111111l_opy_
            )
    except Exception as e:
        logger.error(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨᷢ").format(str(e)))
    return bstack1111lllll1_opy_(self, *args, **kwargs)
def bstack111l1lll111_opy_(bstack1111lll1l11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l111111ll_opy_(bstack1111lll1l11_opy_, bstack111111l_opy_ (u"ࠢࠣᷣ"))
        if proxies and proxies.get(bstack111111l_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢᷤ")):
            parsed_url = urlparse(proxies.get(bstack111111l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣᷥ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack111111l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ᷦ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack111111l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧᷧ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack111111l_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨᷨ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack111111l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩᷩ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l11111lll_opy_(bstack1111lll1l11_opy_):
    bstack111l1l1lll1_opy_ = {
        bstack11l11lll1l1_opy_[bstack1111l1l1lll_opy_]: bstack1111lll1l11_opy_[bstack1111l1l1lll_opy_]
        for bstack1111l1l1lll_opy_ in bstack1111lll1l11_opy_
        if bstack1111l1l1lll_opy_ in bstack11l11lll1l1_opy_
    }
    bstack111l1l1lll1_opy_[bstack111111l_opy_ (u"ࠢࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠢᷪ")] = bstack111l1lll111_opy_(bstack1111lll1l11_opy_, bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣᷫ")))
    bstack111l11lll1l_opy_ = [element.lower() for element in bstack11l11llllll_opy_]
    bstack1111lllll11_opy_(bstack111l1l1lll1_opy_, bstack111l11lll1l_opy_)
    return bstack111l1l1lll1_opy_
def bstack1111lllll11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack111111l_opy_ (u"ࠤ࠭࠮࠯࠰ࠢᷬ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111lllll11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111lllll11_opy_(item, keys)
def bstack1ll11llllll_opy_():
    bstack1111lllll1l_opy_ = [os.environ.get(bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡍࡑࡋࡓࡠࡆࡌࡖࠧᷭ")), os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠦࢃࠨᷮ")), bstack111111l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᷯ")), os.path.join(bstack111111l_opy_ (u"࠭࠯ࡵ࡯ࡳࠫᷰ"), bstack111111l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᷱ"))]
    for path in bstack1111lllll1l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack111111l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣᷲ") + str(path) + bstack111111l_opy_ (u"ࠤࠪࠤࡪࡾࡩࡴࡶࡶ࠲ࠧᷳ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack111111l_opy_ (u"ࠥࡋ࡮ࡼࡩ࡯ࡩࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠡࡨࡲࡶࠥ࠭ࠢᷴ") + str(path) + bstack111111l_opy_ (u"ࠦࠬࠨ᷵"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack111111l_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࠫࠧ᷶") + str(path) + bstack111111l_opy_ (u"ࠨࠧࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡫ࡥࡸࠦࡴࡩࡧࠣࡶࡪࡷࡵࡪࡴࡨࡨࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵ࠱᷷ࠦ"))
            else:
                logger.debug(bstack111111l_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࠨࠤ᷸") + str(path) + bstack111111l_opy_ (u"ࠣࠩࠣࡻ࡮ࡺࡨࠡࡹࡵ࡭ࡹ࡫ࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱ࠲᷹ࠧ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack111111l_opy_ (u"ࠤࡒࡴࡪࡸࡡࡵ࡫ࡲࡲࠥࡹࡵࡤࡥࡨࡩࡩ࡫ࡤࠡࡨࡲࡶ᷺ࠥ࠭ࠢ") + str(path) + bstack111111l_opy_ (u"ࠥࠫ࠳ࠨ᷻"))
            return path
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡺࡶࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡱࡣࡷ࡬ࢂ࠭࠺ࠡࠤ᷼") + str(e) + bstack111111l_opy_ (u"ࠧࠨ᷽"))
    logger.debug(bstack111111l_opy_ (u"ࠨࡁ࡭࡮ࠣࡴࡦࡺࡨࡴࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠥ᷾"))
    return None
@measure(event_name=EVENTS.bstack11l1l11llll_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1l1l1l11l11_opy_(binary_path, bstack1l1ll1111ll_opy_, bs_config):
    logger.debug(bstack111111l_opy_ (u"ࠢࡄࡷࡵࡶࡪࡴࡴࠡࡅࡏࡍࠥࡖࡡࡵࡪࠣࡪࡴࡻ࡮ࡥ࠼ࠣࡿࢂࠨ᷿").format(binary_path))
    bstack111l1l1llll_opy_ = bstack111111l_opy_ (u"ࠨࠩḀ")
    bstack1111ll11l1l_opy_ = {
        bstack111111l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḁ"): __version__,
        bstack111111l_opy_ (u"ࠥࡳࡸࠨḂ"): platform.system(),
        bstack111111l_opy_ (u"ࠦࡴࡹ࡟ࡢࡴࡦ࡬ࠧḃ"): platform.machine(),
        bstack111111l_opy_ (u"ࠧࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠥḄ"): bstack111111l_opy_ (u"࠭࠰ࠨḅ"),
        bstack111111l_opy_ (u"ࠢࡴࡦ࡮ࡣࡱࡧ࡮ࡨࡷࡤ࡫ࡪࠨḆ"): bstack111111l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨḇ")
    }
    bstack111l1llllll_opy_(bstack1111ll11l1l_opy_)
    try:
        if binary_path:
            bstack1111ll11l1l_opy_[bstack111111l_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧḈ")] = subprocess.check_output([binary_path, bstack111111l_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦḉ")]).strip().decode(bstack111111l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪḊ"))
        response = requests.request(
            bstack111111l_opy_ (u"ࠬࡍࡅࡕࠩḋ"),
            url=bstack11ll11l11_opy_(bstack11l1l1l111l_opy_),
            headers=None,
            auth=(bs_config[bstack111111l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨḌ")], bs_config[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪḍ")]),
            json=None,
            params=bstack1111ll11l1l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack111111l_opy_ (u"ࠨࡷࡵࡰࠬḎ") in data.keys() and bstack111111l_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡦࡢࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḏ") in data.keys():
            logger.debug(bstack111111l_opy_ (u"ࠥࡒࡪ࡫ࡤࠡࡶࡲࠤࡺࡶࡤࡢࡶࡨࠤࡧ࡯࡮ࡢࡴࡼ࠰ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠦḐ").format(bstack1111ll11l1l_opy_[bstack111111l_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩḑ")]))
            if bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣ࡚ࡘࡌࠨḒ") in os.environ:
                logger.debug(bstack111111l_opy_ (u"ࠨࡓ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡥࡸࠦࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠢ࡬ࡷࠥࡹࡥࡵࠤḓ"))
                data[bstack111111l_opy_ (u"ࠧࡶࡴ࡯ࠫḔ")] = os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫḕ")]
            bstack1111ll1l111_opy_ = bstack1111l1l11ll_opy_(data[bstack111111l_opy_ (u"ࠩࡸࡶࡱ࠭Ḗ")], bstack1l1ll1111ll_opy_)
            bstack111l1l1llll_opy_ = os.path.join(bstack1l1ll1111ll_opy_, bstack1111ll1l111_opy_)
            os.chmod(bstack111l1l1llll_opy_, 0o777) # bstack1111l1ll1ll_opy_ permission
            return bstack111l1l1llll_opy_
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦ࡮ࡦࡹࠣࡗࡉࡑࠠࡼࡿࠥḗ").format(e))
    return binary_path
def bstack111l1llllll_opy_(bstack1111ll11l1l_opy_):
    try:
        if bstack111111l_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪḘ") not in bstack1111ll11l1l_opy_[bstack111111l_opy_ (u"ࠬࡵࡳࠨḙ")].lower():
            return
        if os.path.exists(bstack111111l_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡴࡹ࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣḚ")):
            with open(bstack111111l_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡵࡳ࠮ࡴࡨࡰࡪࡧࡳࡦࠤḛ"), bstack111111l_opy_ (u"ࠣࡴࠥḜ")) as f:
                bstack111l11l1l1l_opy_ = {}
                for line in f:
                    if bstack111111l_opy_ (u"ࠤࡀࠦḝ") in line:
                        key, value = line.rstrip().split(bstack111111l_opy_ (u"ࠥࡁࠧḞ"), 1)
                        bstack111l11l1l1l_opy_[key] = value.strip(bstack111111l_opy_ (u"ࠫࠧࡢࠧࠨḟ"))
                bstack1111ll11l1l_opy_[bstack111111l_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬḠ")] = bstack111l11l1l1l_opy_.get(bstack111111l_opy_ (u"ࠨࡉࡅࠤḡ"), bstack111111l_opy_ (u"ࠢࠣḢ"))
        elif os.path.exists(bstack111111l_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵ࡡ࡭ࡲ࡬ࡲࡪ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢḣ")):
            bstack1111ll11l1l_opy_[bstack111111l_opy_ (u"ࠩࡧ࡭ࡸࡺࡲࡰࠩḤ")] = bstack111111l_opy_ (u"ࠪࡥࡱࡶࡩ࡯ࡧࠪḥ")
    except Exception as e:
        logger.debug(bstack111111l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡩ࡯ࡳࡵࡴࡲࠤࡴ࡬ࠠ࡭࡫ࡱࡹࡽࠨḦ") + e)
@measure(event_name=EVENTS.bstack11l1l1l1111_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1111l1l11ll_opy_(bstack1111llllll1_opy_, bstack111l11lllll_opy_):
    logger.debug(bstack111111l_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱ࠿ࠦࠢḧ") + str(bstack1111llllll1_opy_) + bstack111111l_opy_ (u"ࠨࠢḨ"))
    zip_path = os.path.join(bstack111l11lllll_opy_, bstack111111l_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡣ࡫࡯࡬ࡦ࠰ࡽ࡭ࡵࠨḩ"))
    bstack1111ll1l111_opy_ = bstack111111l_opy_ (u"ࠨࠩḪ")
    with requests.get(bstack1111llllll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack111111l_opy_ (u"ࠤࡺࡦࠧḫ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack111111l_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࠲ࠧḬ"))
    with zipfile.ZipFile(zip_path, bstack111111l_opy_ (u"ࠫࡷ࠭ḭ")) as zip_ref:
        bstack1111lllllll_opy_ = zip_ref.namelist()
        if len(bstack1111lllllll_opy_) > 0:
            bstack1111ll1l111_opy_ = bstack1111lllllll_opy_[0] # bstack111l1ll111l_opy_ bstack11l11llll11_opy_ will be bstack1llll11ll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l11lllll_opy_)
        logger.debug(bstack111111l_opy_ (u"ࠧࡌࡩ࡭ࡧࡶࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡩࡽࡺࡲࡢࡥࡷࡩࡩࠦࡴࡰࠢࠪࠦḮ") + str(bstack111l11lllll_opy_) + bstack111111l_opy_ (u"ࠨࠧࠣḯ"))
    os.remove(zip_path)
    return bstack1111ll1l111_opy_
def get_cli_dir():
    bstack1111ll1ll11_opy_ = bstack1ll11llllll_opy_()
    if bstack1111ll1ll11_opy_:
        bstack1l1ll1111ll_opy_ = os.path.join(bstack1111ll1ll11_opy_, bstack111111l_opy_ (u"ࠢࡤ࡮࡬ࠦḰ"))
        if not os.path.exists(bstack1l1ll1111ll_opy_):
            os.makedirs(bstack1l1ll1111ll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1ll1111ll_opy_
    else:
        raise FileNotFoundError(bstack111111l_opy_ (u"ࠣࡐࡲࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻ࠱ࠦḱ"))
def bstack1l11ll1ll1l_opy_(bstack1l1ll1111ll_opy_):
    bstack111111l_opy_ (u"ࠤࠥࠦࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡰࠣࡥࠥࡽࡲࡪࡶࡤࡦࡱ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠱ࠦࠧࠨḲ")
    bstack1111ll1l1l1_opy_ = [
        os.path.join(bstack1l1ll1111ll_opy_, f)
        for f in os.listdir(bstack1l1ll1111ll_opy_)
        if os.path.isfile(os.path.join(bstack1l1ll1111ll_opy_, f)) and f.startswith(bstack111111l_opy_ (u"ࠥࡦ࡮ࡴࡡࡳࡻ࠰ࠦḳ"))
    ]
    if len(bstack1111ll1l1l1_opy_) > 0:
        return max(bstack1111ll1l1l1_opy_, key=os.path.getmtime) # get bstack1111ll1ll1l_opy_ binary
    return bstack111111l_opy_ (u"ࠦࠧḴ")
def bstack111ll11111l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1ll1l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1ll1l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lll1111l_opy_(data, keys, default=None):
    bstack111111l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡙ࠥࡡࡧࡧ࡯ࡽࠥ࡭ࡥࡵࠢࡤࠤࡳ࡫ࡳࡵࡧࡧࠤࡻࡧ࡬ࡶࡧࠣࡪࡷࡵ࡭ࠡࡣࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡰࡴࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡢࡶࡤ࠾࡚ࠥࡨࡦࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦ࡯ࡳࠢ࡯࡭ࡸࡺࠠࡵࡱࠣࡸࡷࡧࡶࡦࡴࡶࡩ࠳ࠐࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣ࡯ࡪࡿࡳ࠻ࠢࡄࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡱࡥࡺࡵ࠲࡭ࡳࡪࡩࡤࡧࡶࠤࡷ࡫ࡰࡳࡧࡶࡩࡳࡺࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡨࡪ࡬ࡡࡶ࡮ࡷ࠾ࠥ࡜ࡡ࡭ࡷࡨࠤࡹࡵࠠࡳࡧࡷࡹࡷࡴࠠࡪࡨࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡸࡥࡵࡷࡵࡲ࠿ࠦࡔࡩࡧࠣࡺࡦࡲࡵࡦࠢࡤࡸࠥࡺࡨࡦࠢࡱࡩࡸࡺࡥࡥࠢࡳࡥࡹ࡮ࠬࠡࡱࡵࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥ࡯ࡦࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠲ࠏࠦࠠࠡࠢࠥࠦࠧḵ")
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