# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111ll11l_opy_
from browserstack_sdk.bstack1lllll1l1_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111llll1_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from bstack_utils.constants import bstack1111ll1l_opy_
from bstack_utils.bstack111111ll_opy_ import bstack111l11ll_opy_
class bstack1lllllll1_opy_:
    def __init__(self, args, logger, bstack111l1lll_opy_, bstack1lll1ll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1lll_opy_ = bstack111l1lll_opy_
        self.bstack1lll1ll1l_opy_ = bstack1lll1ll1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1llll1lll_opy_ = []
        self.bstack1lllll111_opy_ = []
        self.bstack1lll1l1ll_opy_ = []
        self.bstack1llll11ll_opy_ = self.bstack1lll1l111_opy_()
        self.bstack111l1l11_opy_ = -1
    def bstack1llll1111_opy_(self, bstack111111l1_opy_):
        self.parse_args()
        self.bstack111l11l1_opy_()
        self.bstack1llll1l11_opy_(bstack111111l1_opy_)
        self.bstack1111lll1_opy_()
    def bstack1111l1ll_opy_(self):
        bstack111111ll_opy_ = bstack111l11ll_opy_.bstack111ll1l1_opy_(self.bstack111l1lll_opy_, self.logger)
        if bstack111111ll_opy_ is None:
            self.logger.warn(bstack11lll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঵"))
            return
        bstack1111l111_opy_ = False
        bstack111111ll_opy_.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤশ"), bstack111111ll_opy_.bstack1111l11l_opy_())
        start_time = time.time()
        if bstack111111ll_opy_.bstack1111l11l_opy_():
            test_files = self.bstack1111llll_opy_()
            bstack1111l111_opy_ = True
            bstack111lll11_opy_ = bstack111111ll_opy_.bstack1llllllll_opy_(test_files)
            if bstack111lll11_opy_:
                self.bstack1llll1lll_opy_ = [os.path.normpath(item).replace(bstack11lll1_opy_ (u"ࠩ࡟ࡠࠬষ"), bstack11lll1_opy_ (u"ࠪ࠳ࠬস")) for item in bstack111lll11_opy_]
                self.__11111l11_opy_()
                bstack111111ll_opy_.bstack1111l1l1_opy_(bstack1111l111_opy_)
                self.logger.info(bstack11lll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤহ").format(self.bstack1llll1lll_opy_))
            else:
                self.logger.info(bstack11lll1_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঺"))
        bstack111111ll_opy_.bstack1111ll11_opy_(bstack11lll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤ঻"), int((time.time() - start_time) * 1000)) # bstack1lll11l11_opy_ to bstack1llllll11_opy_
    def __11111l11_opy_(self):
        bstack11lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡰ࡭ࡣࡦࡩࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭ࡹࠠࡪࡰࠣࡇࡑࡏࠠࡧ࡮ࡤ࡫ࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭ࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡩࡷࡼࡥࡳࠢࡵࡩࡹࡻࡲ࡯ࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡦࡪ࡮ࡨࠤࡳࡧ࡭ࡦࡵ࠯ࠤࡦࡴࡤࠡࡹࡨࠤࡸ࡯࡭ࡱ࡮ࡼࠤࡺࡶࡤࡢࡶࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡆࡐࡎࠦࡡࡳࡩࡶࠤࡹࡵࠠࡶࡵࡨࠤࡹ࡮࡯ࡴࡧࠣࡪ࡮ࡲࡥࡴ࠰࡙ࠣࡸ࡫ࡲࠨࡵࠣࡪ࡮ࡲࡴࡦࡴ࡬ࡲ࡬ࠦࡦ࡭ࡣࡪࡷࠥ࠮࠭࡮࠮ࠣ࠱ࡰ࠯ࠠࡳࡧࡰࡥ࡮ࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸࡦࡩࡴࠡࡣࡱࡨࠥࡽࡩ࡭࡮ࠣࡦࡪࠦࡡࡱࡲ࡯࡭ࡪࡪࠠ࡯ࡣࡷࡹࡷࡧ࡬࡭ࡻࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡾࡺࡥࡴࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤ়ࠥࠦࠠࠡࠢࠥࠦࠧ")
        try:
            if not self.bstack1llll1lll_opy_:
                self.logger.debug(bstack11lll1_opy_ (u"ࠣࡐࡲࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡳࡥࡹ࡮ࠠࡵࡱࠣࡷࡪࡺࠢঽ"))
                return
            bstack1111111l_opy_ = []
            bstack111l1ll1_opy_ = []
            for flag in self.bstack1lllll111_opy_:
                if flag.startswith(bstack11lll1_opy_ (u"ࠩ࠰ࠫা")):
                    bstack1111111l_opy_.append(flag)
                    continue
                bstack111l111l_opy_ = False
                if bstack11lll1_opy_ (u"ࠪ࠾࠿࠭ি") in flag:
                    bstack111l111l_opy_ = True
                elif flag.endswith(bstack11lll1_opy_ (u"ࠫ࠳ࡶࡹࠨী")):
                    bstack111l111l_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11lll1_opy_ (u"ࠬ࠴ࡰࡺࠩু"))):
                        bstack111l111l_opy_ = True
                if not bstack111l111l_opy_:
                    bstack1111111l_opy_.append(flag)
                else:
                    bstack111l1ll1_opy_.append(flag)
            bstack1111111l_opy_.extend(self.bstack1llll1lll_opy_)
            self.bstack1lllll111_opy_ = bstack1111111l_opy_
            self.logger.info(bstack11lll1_opy_ (u"ࠨࡕࡱࡦࡤࡸࡪࡪࠠࡄࡎࡌࠤ࡫ࡲࡡࡨࡵࠣࡥ࡫ࡺࡥࡳࠢࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠼ࠣࡿࢂࠨূ").format(self.bstack1lllll111_opy_))
        except Exception as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡶࡩࡱ࡫ࡣࡵࡱࡵࡷ࠿ࠦࡻࡾࠤৃ").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll11ll1_opy_():
        import importlib
        if getattr(importlib, bstack11lll1_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ৄ"), False):
            bstack111l1111_opy_ = importlib.find_loader(bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ৅"))
        else:
            bstack111l1111_opy_ = importlib.util.find_spec(bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ৆"))
    def bstack1llllll1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l1l11_opy_ = -1
        if self.bstack1lll1ll1l_opy_ and bstack11lll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫে") in self.bstack111l1lll_opy_:
            self.bstack111l1l11_opy_ = int(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬৈ")])
        try:
            bstack1llll111l_opy_ = [bstack11lll1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ৉"), bstack11lll1_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪ৊"), bstack11lll1_opy_ (u"ࠨ࠯ࡳࠫো")]
            if self.bstack111l1l11_opy_ >= 0:
                bstack1llll111l_opy_.extend([bstack11lll1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪৌ"), bstack11lll1_opy_ (u"ࠪ࠱ࡳ্࠭")])
            for arg in bstack1llll111l_opy_:
                self.bstack1llllll1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111l11l1_opy_(self):
        bstack1lllll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lllll111_opy_ = bstack1lllll111_opy_
        return self.bstack1lllll111_opy_
    def bstack1lll1ll11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll11ll1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111llll1_opy_)
    def bstack1llll1l11_opy_(self, bstack111111l1_opy_):
        bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
        if bstack111111l1_opy_:
            self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨৎ"))
            self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"࡚ࠬࡲࡶࡧࠪ৏"))
        if bstack1lll1l11l_opy_.bstack111ll111_opy_():
            self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ৐"))
            self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠧࡕࡴࡸࡩࠬ৑"))
        self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠨ࠯ࡳࠫ৒"))
        self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧ৓"))
        self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬ৔"))
        self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ৕"))
        if self.bstack111l1l11_opy_ > 1:
            self.bstack1lllll111_opy_.append(bstack11lll1_opy_ (u"ࠬ࠳࡮ࠨ৖"))
            self.bstack1lllll111_opy_.append(str(self.bstack111l1l11_opy_))
    def bstack1111lll1_opy_(self):
        if bstack11111lll_opy_.bstack11111111_opy_(self.bstack111l1lll_opy_):
             self.bstack1lllll111_opy_ += [
                bstack1111ll1l_opy_.get(bstack11lll1_opy_ (u"࠭ࡲࡦࡴࡸࡲࠬৗ")), str(bstack11111lll_opy_.bstack111l1l1l_opy_(self.bstack111l1lll_opy_)),
                bstack1111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭৘")), str(bstack1111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࠭ࡥࡧ࡯ࡥࡾ࠭৙")))
            ]
    def bstack11111ll1_opy_(self):
        bstack1lll1l1ll_opy_ = []
        for spec in self.bstack1llll1lll_opy_:
            bstack1lll111l1_opy_ = [spec]
            bstack1lll111l1_opy_ += self.bstack1lllll111_opy_
            bstack1lll1l1ll_opy_.append(bstack1lll111l1_opy_)
        self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
        return bstack1lll1l1ll_opy_
    def bstack1lll1l111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll11ll_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll11ll_opy_ = False
        return self.bstack1llll11ll_opy_
    def bstack1llll11l1_opy_(self):
        bstack11lll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৚")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11l1llll_opy_
            bstack1lll1llll_opy_ = bstack11l1llll_opy_(bstack11ll11ll_opy_=self.bstack1lllll111_opy_)
            if not bstack1lll1llll_opy_.get(bstack11lll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ৛"), False):
                self.logger.error(bstack11lll1_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡦࡳࡺࡴࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤড়").format(bstack1lll1llll_opy_.get(bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫঢ়"), bstack11lll1_opy_ (u"࠭ࡕ࡯࡭ࡱࡳࡼࡴࠠࡦࡴࡵࡳࡷ࠭৞"))))
                return 0
            count = bstack1lll1llll_opy_.get(bstack11lll1_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭য়"), 0)
            test_files = bstack1lll1llll_opy_.get(bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬৠ"), [])
            self.logger.info(bstack11lll1_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠽ࠤࢀࢃࠢৡ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢৢ").format(e))
            return 0
    def bstack1lll11lll_opy_(self, bstack1llll1ll1_opy_, bstack1llll1111_opy_):
        bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫৣ")] = self.bstack111l1lll_opy_
        multiprocessing.set_start_method(bstack11lll1_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫ৤"))
        bstack111lll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lll111ll_opy_ = manager.list()
        if bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৥") in self.bstack111l1lll_opy_:
            for index, platform in enumerate(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ০")]):
                bstack111lll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1llll1ll1_opy_,
                                                            args=(self.bstack1lllll111_opy_, bstack1llll1111_opy_, bstack1lll111ll_opy_)))
            bstack111ll1ll_opy_ = len(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ১")])
        else:
            bstack111lll1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1llll1ll1_opy_,
                                                        args=(self.bstack1lllll111_opy_, bstack1llll1111_opy_, bstack1lll111ll_opy_)))
            bstack111ll1ll_opy_ = 1
        i = 0
        for t in bstack111lll1l_opy_:
            os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ২")] = str(i)
            if bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৩") in self.bstack111l1lll_opy_:
                os.environ[bstack11lll1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ৪")] = json.dumps(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৫")][i % bstack111ll1ll_opy_])
            i += 1
            t.start()
        for t in bstack111lll1l_opy_:
            t.join()
        return list(bstack1lll111ll_opy_)
    @staticmethod
    def bstack1lllll1ll_opy_(driver, bstack1llll1l1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৬"), None)
        if item and getattr(item, bstack11lll1_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ৭"), None) and not getattr(item, bstack11lll1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪ৮"), False):
            logger.info(
                bstack11lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ৯"))
            bstack1lllll11l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111ll11l_opy_.bstack1lll1lll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1111llll_opy_(self):
        bstack11lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤৰ")
        try:
            from browserstack_sdk.bstack11ll1lll_opy_ import bstack11l1llll_opy_
            bstack1lll11l1l_opy_ = bstack11l1llll_opy_(bstack11ll11ll_opy_=self.bstack1lllll111_opy_)
            if not bstack1lll11l1l_opy_.get(bstack11lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬৱ"), False):
                self.logger.error(bstack11lll1_opy_ (u"࡚ࠧࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৲").format(bstack1lll11l1l_opy_.get(bstack11lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৳"), bstack11lll1_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৴"))))
                return []
            test_files = bstack1lll11l1l_opy_.get(bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৵"), [])
            count = bstack1lll11l1l_opy_.get(bstack11lll1_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৶"), 0)
            self.logger.debug(bstack11lll1_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨ৷").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦ৸").format(e))
            return []