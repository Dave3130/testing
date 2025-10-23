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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1llll111l_opy_
import subprocess
import re
from browserstack_sdk.bstack1111l1ll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11111111_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack1lll1ll11_opy_
from bstack_utils.constants import bstack1llllllll_opy_
from bstack_utils.bstack111lll11_opy_ import bstack11111ll1_opy_
class bstack1llll1111_opy_:
    bstack111ll111_opy_ = bstack111111l_opy_ (u"ࡲࠨ࠾ࡐࡳࡩࡻ࡬ࡦࠢࠫ࡟ࡣࡄ࡝ࠬࠫࡁࠫ঒")  # bstack1111ll1l_opy_ lines bstack1llllll_opy_ <Module path/to/bstack111l1l11_opy_.py> in pytest --collect-bstack1llll11ll_opy_ output
    def __init__(self, args, logger, bstack111l11ll_opy_, bstack1lll1lll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l11ll_opy_ = bstack111l11ll_opy_
        self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llllll1l_opy_ = []
        self.bstack1lllll1l1_opy_ = []
        self.bstack111llll1_opy_ = []
        self.bstack111l1ll1_opy_ = self.bstack111l1l1l_opy_()
        self.bstack1lll1ll1l_opy_ = -1
    def bstack111ll1ll_opy_(self, bstack11l111ll_opy_):
        self.parse_args()
        self.bstack1llll1lll_opy_()
        self.bstack11l11lll_opy_(bstack11l111ll_opy_)
        self.bstack111111l1_opy_()
    def bstack111lll1l_opy_(self):
        bstack111lll11_opy_ = bstack11111ll1_opy_.bstack111l111l_opy_(self.bstack111l11ll_opy_, self.logger)
        if bstack111lll11_opy_ is None:
            self.logger.warn(bstack111111l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦও"))
            return
        bstack1111l11l_opy_ = False
        bstack111lll11_opy_.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥঔ"), bstack111lll11_opy_.bstack1111l111_opy_())
        start_time = time.time()
        if bstack111lll11_opy_.bstack1111l111_opy_():
            test_files = self.bstack11111l1l_opy_()
            bstack1111l11l_opy_ = True
            bstack1lllll111_opy_ = bstack111lll11_opy_.bstack11l11l1l_opy_(test_files)
            if bstack1lllll111_opy_:
                self.bstack1llllll1l_opy_ = [os.path.normpath(item).replace(bstack111111l_opy_ (u"ࠪࡠࡡ࠭ক"), bstack111111l_opy_ (u"ࠫ࠴࠭খ")) for item in bstack1lllll111_opy_]
                self.__1llll1l11_opy_()
                bstack111lll11_opy_.bstack1lll1llll_opy_(bstack1111l11l_opy_)
                self.logger.info(bstack111111l_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥগ").format(self.bstack1llllll1l_opy_))
            else:
                self.logger.info(bstack111111l_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦঘ"))
        bstack111lll11_opy_.bstack111111ll_opy_(bstack111111l_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥঙ"), int((time.time() - start_time) * 1000)) # bstack1llll1l1l_opy_ to bstack1llll11l1_opy_
    def __1llll1l11_opy_(self):
        bstack111111l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡦࡳࡱࡲࡥࡤࡶࠣࡥࡱࡲࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧচ")
        bstack1lllll11l_opy_ = []
        for bstack111l1l11_opy_ in self.bstack1llllll1l_opy_:
            bstack111l1111_opy_ = [bstack111111l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤছ"), bstack111l1l11_opy_, bstack111111l_opy_ (u"ࠥ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼࠦজ"), bstack111111l_opy_ (u"ࠦ࠲ࡷࠢঝ")]
            result = subprocess.run(bstack111l1111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                self.logger.error(bstack1llll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡰࡲࡨࡪ࡯ࡤࡴࠢࡩࡳࡷࠦࡻࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࢀ࠾ࠥࢁࡲࡦࡵࡸࡰࡹ࠴ࡳࡵࡦࡨࡶࡷࢃࠢঞ"))
                continue
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and not line.startswith(bstack111111l_opy_ (u"ࠨ࠼ࠣট")) and bstack111111l_opy_ (u"ࠢ࠻࠼ࠥঠ") in line:
                    bstack1lllll11l_opy_.append(line)
        os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔࠩড")] = json.dumps(bstack1lllll11l_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll1l1ll_opy_():
        import importlib
        if getattr(importlib, bstack111111l_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧঢ"), False):
            bstack11l111l1_opy_ = importlib.find_loader(bstack111111l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬণ"))
        else:
            bstack11l111l1_opy_ = importlib.util.find_spec(bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ত"))
    def bstack111ll1l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lll1ll1l_opy_ = -1
        if self.bstack1lll1lll1_opy_ and bstack111111l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬথ") in self.bstack111l11ll_opy_:
            self.bstack1lll1ll1l_opy_ = int(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭দ")])
        try:
            bstack1111ll11_opy_ = [bstack111111l_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩধ"), bstack111111l_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫন"), bstack111111l_opy_ (u"ࠩ࠰ࡴࠬ঩")]
            if self.bstack1lll1ll1l_opy_ >= 0:
                bstack1111ll11_opy_.extend([bstack111111l_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫপ"), bstack111111l_opy_ (u"ࠫ࠲ࡴࠧফ")])
            for arg in bstack1111ll11_opy_:
                self.bstack111ll1l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1llll1lll_opy_(self):
        bstack1lllll1l1_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lllll1l1_opy_ = bstack1lllll1l1_opy_
        return self.bstack1lllll1l1_opy_
    def bstack1111llll_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll1l1ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11111111_opy_)
    def bstack11l11lll_opy_(self, bstack11l111ll_opy_):
        bstack11111lll_opy_ = Config.bstack111l111l_opy_()
        if bstack11l111ll_opy_:
            self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩব"))
            self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"࠭ࡔࡳࡷࡨࠫভ"))
        if bstack11111lll_opy_.bstack11l1l11l_opy_():
            self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ম"))
            self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠨࡖࡵࡹࡪ࠭য"))
        self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠩ࠰ࡴࠬর"))
        self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨ঱"))
        self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ল"))
        self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ঳"))
        if self.bstack1lll1ll1l_opy_ > 1:
            self.bstack1lllll1l1_opy_.append(bstack111111l_opy_ (u"࠭࠭࡯ࠩ঴"))
            self.bstack1lllll1l1_opy_.append(str(self.bstack1lll1ll1l_opy_))
    def bstack111111l1_opy_(self):
        if bstack1lll1ll11_opy_.bstack1111lll1_opy_(self.bstack111l11ll_opy_):
             self.bstack1lllll1l1_opy_ += [
                bstack1llllllll_opy_.get(bstack111111l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭঵")), str(bstack1lll1ll11_opy_.bstack1111111l_opy_(self.bstack111l11ll_opy_)),
                bstack1llllllll_opy_.get(bstack111111l_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧশ")), str(bstack1llllllll_opy_.get(bstack111111l_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧষ")))
            ]
    def bstack1lllll1ll_opy_(self):
        bstack111llll1_opy_ = []
        for spec in self.bstack1llllll1l_opy_:
            bstack11l11l11_opy_ = [spec]
            bstack11l11l11_opy_ += self.bstack1lllll1l1_opy_
            bstack111llll1_opy_.append(bstack11l11l11_opy_)
        self.bstack111llll1_opy_ = bstack111llll1_opy_
        return bstack111llll1_opy_
    def bstack111l1l1l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1ll1_opy_ = False
        return self.bstack111l1ll1_opy_
    def bstack11l1111l_opy_(self):
        bstack111111l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡶ࡫ࡩࡲࠦࡵࡴ࡫ࡱ࡫ࠥࡶࡹࡵࡧࡶࡸࠬࡹࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠡࡨ࡯ࡥ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨস")
        try:
            self.logger.info(bstack111111l_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢহ"))
            bstack111l1111_opy_ = [bstack111111l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ঺"), *self.bstack1lllll1l1_opy_, bstack111111l_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢ঻")]
            result = subprocess.run(bstack111l1111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                self.logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࡳ࠻ࠢࡾࢁ়ࠧ").format(result.stderr))
                return 0
            test_count = result.stdout.count(bstack111111l_opy_ (u"ࠣ࠾ࡉࡹࡳࡩࡴࡪࡱࡱࠤࠧঽ"))
            self.logger.info(bstack111111l_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠽ࠤࢀࢃࠢা").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢি").format(e))
            return 0
    def bstack1llllll11_opy_(self, bstack11l1l111_opy_, bstack111ll1ll_opy_):
        bstack111ll1ll_opy_[bstack111111l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫী")] = self.bstack111l11ll_opy_
        multiprocessing.set_start_method(bstack111111l_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫু"))
        bstack11l11111_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l11l1_opy_ = manager.list()
        if bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩূ") in self.bstack111l11ll_opy_:
            for index, platform in enumerate(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪৃ")]):
                bstack11l11111_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11l1l111_opy_,
                                                            args=(self.bstack1lllll1l1_opy_, bstack111ll1ll_opy_, bstack111l11l1_opy_)))
            bstack111lllll_opy_ = len(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৄ")])
        else:
            bstack11l11111_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11l1l111_opy_,
                                                        args=(self.bstack1lllll1l1_opy_, bstack111ll1ll_opy_, bstack111l11l1_opy_)))
            bstack111lllll_opy_ = 1
        i = 0
        for t in bstack11l11111_opy_:
            os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ৅")] = str(i)
            if bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆") in self.bstack111l11ll_opy_:
                os.environ[bstack111111l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬে")] = json.dumps(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨৈ")][i % bstack111lllll_opy_])
            i += 1
            t.start()
        for t in bstack11l11111_opy_:
            t.join()
        return list(bstack111l11l1_opy_)
    @staticmethod
    def bstack111l1lll_opy_(driver, bstack111ll11l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৉"), None)
        if item and getattr(item, bstack111111l_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ৊"), None) and not getattr(item, bstack111111l_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪো"), False):
            logger.info(
                bstack111111l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣৌ"))
            bstack11l11ll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1llll111l_opy_.bstack1lllllll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack11111l1l_opy_(self):
        bstack111111l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧࠤࡧࡿࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡵࡵࡵࡲࡸࡸࠥࡵࡦࠡࡲࡼࡸࡪࡹࡴࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡓࡵࡴࡦ࠼ࠣࡘ࡭࡫ࠠࡳࡧࡪࡩࡽࠦࡰࡢࡶࡷࡩࡷࡴࠠࡶࡵࡨࡨࠥ࡮ࡥࡳࡧࠣࡨࡪࡶࡥ࡯ࡦࡶࠤࡴࡴࠠࡱࡻࡷࡩࡸࡺࠧࡴࠢࡲࡹࡹࡶࡵࡵࠢࡩࡳࡷࡳࡡࡵࠢࡩࡳࡷࠦ࠼ࡎࡱࡧࡹࡱ࡫ࠠ࠯࠰࠱ࡂࠥࡲࡩ࡯ࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ্")
        try:
            bstack111l1111_opy_ = [bstack111111l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦৎ"), *self.bstack1lllll1l1_opy_, bstack111111l_opy_ (u"ࠧ࠳࠭ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡱࡱࡰࡾࠨ৏")]
            result = subprocess.run(bstack111l1111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                self.logger.error(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠤ৐").format(result.stderr))
                return []
            file_names = set(re.findall(self.bstack111ll111_opy_, result.stdout))
            file_names = sorted(file_names)
            return list(file_names)
        except Exception as e:
            self.logger.error(bstack1llll1ll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀ࡫ࡽࠣ৑"))
            return []