# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from browserstack_sdk.bstack11111l11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111lll11_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack111ll1l1_opy_
from bstack_utils.constants import bstack1lll1l1ll_opy_
from bstack_utils.bstack111ll11l_opy_ import bstack1llll11ll_opy_
class bstack1lllll11l_opy_:
    def __init__(self, args, logger, bstack1111l1ll_opy_, bstack1llll111l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
        self.bstack1llll111l_opy_ = bstack1llll111l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111111l1_opy_ = []
        self.bstack1lllll111_opy_ = []
        self.bstack1lll1l111_opy_ = []
        self.bstack1lll1l1l1_opy_ = self.bstack111l11ll_opy_()
        self.bstack11111lll_opy_ = -1
    def bstack1llll1l1l_opy_(self, bstack1111111l_opy_):
        self.parse_args()
        self.bstack1lll111ll_opy_()
        self.bstack111l11l1_opy_(bstack1111111l_opy_)
        self.bstack1111ll11_opy_()
    def bstack1lll1ll1l_opy_(self):
        bstack111ll11l_opy_ = bstack1llll11ll_opy_.bstack1llll1lll_opy_(self.bstack1111l1ll_opy_, self.logger)
        if bstack111ll11l_opy_ is None:
            self.logger.warn(bstack11l1l11_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঵"))
            return
        bstack111l1ll1_opy_ = False
        bstack111ll11l_opy_.bstack1lll1ll11_opy_(bstack11l1l11_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤশ"), bstack111ll11l_opy_.bstack1111l1l1_opy_())
        start_time = time.time()
        if bstack111ll11l_opy_.bstack1111l1l1_opy_():
            test_files = self.bstack111l1l11_opy_()
            bstack111l1ll1_opy_ = True
            bstack1llll1l11_opy_ = bstack111ll11l_opy_.bstack1lllll1ll_opy_(test_files)
            if bstack1llll1l11_opy_:
                self.bstack111111l1_opy_ = [os.path.normpath(item).replace(bstack11l1l11_opy_ (u"ࠩ࡟ࡠࠬষ"), bstack11l1l11_opy_ (u"ࠪ࠳ࠬস")) for item in bstack1llll1l11_opy_]
                self.__111lll1l_opy_()
                bstack111ll11l_opy_.bstack1llllll1l_opy_(bstack111l1ll1_opy_)
                self.logger.info(bstack11l1l11_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤহ").format(self.bstack111111l1_opy_))
            else:
                self.logger.info(bstack11l1l11_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঺"))
        bstack111ll11l_opy_.bstack1lll1ll11_opy_(bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤ঻"), int((time.time() - start_time) * 1000)) # bstack1lll11ll1_opy_ to bstack1111llll_opy_
    def __111lll1l_opy_(self):
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡰ࡭ࡣࡦࡩࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭ࡹࠠࡪࡰࠣࡇࡑࡏࠠࡧ࡮ࡤ࡫ࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭ࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡩࡷࡼࡥࡳࠢࡵࡩࡹࡻࡲ࡯ࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡦࡪ࡮ࡨࠤࡳࡧ࡭ࡦࡵ࠯ࠤࡦࡴࡤࠡࡹࡨࠤࡸ࡯࡭ࡱ࡮ࡼࠤࡺࡶࡤࡢࡶࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡆࡐࡎࠦࡡࡳࡩࡶࠤࡹࡵࠠࡶࡵࡨࠤࡹ࡮࡯ࡴࡧࠣࡪ࡮ࡲࡥࡴ࠰࡙ࠣࡸ࡫ࡲࠨࡵࠣࡪ࡮ࡲࡴࡦࡴ࡬ࡲ࡬ࠦࡦ࡭ࡣࡪࡷࠥ࠮࠭࡮࠮ࠣ࠱ࡰ࠯ࠠࡳࡧࡰࡥ࡮ࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸࡦࡩࡴࠡࡣࡱࡨࠥࡽࡩ࡭࡮ࠣࡦࡪࠦࡡࡱࡲ࡯࡭ࡪࡪࠠ࡯ࡣࡷࡹࡷࡧ࡬࡭ࡻࠣࡨࡺࡸࡩ࡯ࡩࠣࡴࡾࡺࡥࡴࡶࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤ়ࠥࠦࠠࠡࠢࠥࠦࠧ")
        try:
            if not self.bstack111111l1_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡐࡲࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡳࡥࡹ࡮ࠠࡵࡱࠣࡷࡪࡺࠢঽ"))
                return
            bstack1llllll11_opy_ = []
            bstack111l1l1l_opy_ = []
            for flag in self.bstack1lllll111_opy_:
                if flag.startswith(bstack11l1l11_opy_ (u"ࠩ࠰ࠫা")):
                    bstack1llllll11_opy_.append(flag)
                    continue
                bstack111ll111_opy_ = False
                if bstack11l1l11_opy_ (u"ࠪ࠾࠿࠭ি") in flag:
                    bstack111ll111_opy_ = True
                elif flag.endswith(bstack11l1l11_opy_ (u"ࠫ࠳ࡶࡹࠨী")):
                    bstack111ll111_opy_ = True
                elif os.path.exists(flag):
                    if os.path.isdir(flag) or (os.path.isfile(flag) and flag.endswith(bstack11l1l11_opy_ (u"ࠬ࠴ࡰࡺࠩু"))):
                        bstack111ll111_opy_ = True
                if not bstack111ll111_opy_:
                    bstack1llllll11_opy_.append(flag)
                else:
                    bstack111l1l1l_opy_.append(flag)
            bstack1llllll11_opy_.extend(self.bstack111111l1_opy_)
            self.bstack1lllll111_opy_ = bstack1llllll11_opy_
            self.logger.info(bstack11l1l11_opy_ (u"ࠨࡕࡱࡦࡤࡸࡪࡪࠠࡄࡎࡌࠤ࡫ࡲࡡࡨࡵࠣࡥ࡫ࡺࡥࡳࠢࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠼ࠣࡿࢂࠨূ").format(self.bstack1lllll111_opy_))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡶࡩࡱ࡫ࡣࡵࡱࡵࡷ࠿ࠦࡻࡾࠤৃ").format(str(e)))
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1lll11l1l_opy_():
        import importlib
        if getattr(importlib, bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ৄ"), False):
            bstack1lll1l11l_opy_ = importlib.find_loader(bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ৅"))
        else:
            bstack1lll1l11l_opy_ = importlib.util.find_spec(bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ৆"))
    def bstack1lll1111l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11111lll_opy_ = -1
        if self.bstack1llll111l_opy_ and bstack11l1l11_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫে") in self.bstack1111l1ll_opy_:
            self.bstack11111lll_opy_ = int(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬৈ")])
        try:
            bstack11111ll1_opy_ = [bstack11l1l11_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ৉"), bstack11l1l11_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪ৊"), bstack11l1l11_opy_ (u"ࠨ࠯ࡳࠫো")]
            if self.bstack11111lll_opy_ >= 0:
                bstack11111ll1_opy_.extend([bstack11l1l11_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪৌ"), bstack11l1l11_opy_ (u"ࠪ࠱ࡳ্࠭")])
            for arg in bstack11111ll1_opy_:
                self.bstack1lll1111l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1lll111ll_opy_(self):
        bstack1lllll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1lllll111_opy_ = bstack1lllll111_opy_
        return self.bstack1lllll111_opy_
    def bstack1lll1lll1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1lll11l1l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111lll11_opy_)
    def bstack111l11l1_opy_(self, bstack1111111l_opy_):
        bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
        if bstack1111111l_opy_:
            self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨৎ"))
            self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"࡚ࠬࡲࡶࡧࠪ৏"))
        if bstack111ll1ll_opy_.bstack111111ll_opy_():
            self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ৐"))
            self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠧࡕࡴࡸࡩࠬ৑"))
        self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠨ࠯ࡳࠫ৒"))
        self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧ৓"))
        self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬ৔"))
        self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ৕"))
        if self.bstack11111lll_opy_ > 1:
            self.bstack1lllll111_opy_.append(bstack11l1l11_opy_ (u"ࠬ࠳࡮ࠨ৖"))
            self.bstack1lllll111_opy_.append(str(self.bstack11111lll_opy_))
    def bstack1111ll11_opy_(self):
        if bstack111ll1l1_opy_.bstack1llll11l1_opy_(self.bstack1111l1ll_opy_):
             self.bstack1lllll111_opy_ += [
                bstack1lll1l1ll_opy_.get(bstack11l1l11_opy_ (u"࠭ࡲࡦࡴࡸࡲࠬৗ")), str(bstack111ll1l1_opy_.bstack1lllllll1_opy_(self.bstack1111l1ll_opy_)),
                bstack1lll1l1ll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭৘")), str(bstack1lll1l1ll_opy_.get(bstack11l1l11_opy_ (u"ࠨࡴࡨࡶࡺࡴ࠭ࡥࡧ࡯ࡥࡾ࠭৙")))
            ]
    def bstack1lll11lll_opy_(self):
        bstack1lll1l111_opy_ = []
        for spec in self.bstack111111l1_opy_:
            bstack1111ll1l_opy_ = [spec]
            bstack1111ll1l_opy_ += self.bstack1lllll111_opy_
            bstack1lll1l111_opy_.append(bstack1111ll1l_opy_)
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
        return bstack1lll1l111_opy_
    def bstack111l11ll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lll1l1l1_opy_ = True
            return True
        except Exception as e:
            self.bstack1lll1l1l1_opy_ = False
        return self.bstack1lll1l1l1_opy_
    def bstack1llll1111_opy_(self):
        bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡸ࡭࡫࡭ࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৚")
        try:
            from browserstack_sdk.bstack11ll1l1l_opy_ import bstack11ll1111_opy_
            bstack111l1lll_opy_ = bstack11ll1111_opy_(bstack11ll11l1_opy_=self.bstack1lllll111_opy_, bstack11ll11ll_opy_=True)
            if not bstack111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ৛"), False):
                self.logger.error(bstack11l1l11_opy_ (u"࡙ࠦ࡫ࡳࡵࠢࡦࡳࡺࡴࡴࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤড়").format(bstack111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫঢ়"), bstack11l1l11_opy_ (u"࠭ࡕ࡯࡭ࡱࡳࡼࡴࠠࡦࡴࡵࡳࡷ࠭৞"))))
                return 0
            count = bstack111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡤࡱࡸࡲࡹ࠭য়"), 0)
            test_files = bstack111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬৠ"), [])
            self.logger.info(bstack11l1l11_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡦࡦ࠽ࠤࢀࢃࠢৡ").format(count))
            return count
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢৢ").format(e))
            return 0
    def bstack11111l1l_opy_(self, bstack11111111_opy_, bstack1llll1l1l_opy_):
        bstack1llll1l1l_opy_[bstack11l1l11_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫৣ")] = self.bstack1111l1ll_opy_
        multiprocessing.set_start_method(bstack11l1l11_opy_ (u"ࠬࡹࡰࡢࡹࡱࠫ৤"))
        bstack1lll111l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l11l_opy_ = manager.list()
        if bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৥") in self.bstack1111l1ll_opy_:
            for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ০")]):
                bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11111111_opy_,
                                                            args=(self.bstack1lllll111_opy_, bstack1llll1l1l_opy_, bstack1111l11l_opy_)))
            bstack1111lll1_opy_ = len(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ১")])
        else:
            bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11111111_opy_,
                                                        args=(self.bstack1lllll111_opy_, bstack1llll1l1l_opy_, bstack1111l11l_opy_)))
            bstack1111lll1_opy_ = 1
        i = 0
        for t in bstack1lll111l1_opy_:
            os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ২")] = str(i)
            if bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৩") in self.bstack1111l1ll_opy_:
                os.environ[bstack11l1l11_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ৪")] = json.dumps(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৫")][i % bstack1111lll1_opy_])
            i += 1
            t.start()
        for t in bstack1lll111l1_opy_:
            t.join()
        return list(bstack1111l11l_opy_)
    @staticmethod
    def bstack1llllllll_opy_(driver, bstack1lll1llll_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ৬"), None)
        if item and getattr(item, bstack11l1l11_opy_ (u"ࠧࡠࡣ࠴࠵ࡾࡥࡴࡦࡵࡷࡣࡨࡧࡳࡦࠩ৭"), None) and not getattr(item, bstack11l1l11_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࡤࡪ࡯࡯ࡧࠪ৮"), False):
            logger.info(
                bstack11l1l11_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠣ৯"))
            bstack111l111l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lllll1l1_opy_.bstack1111l111_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111l1l11_opy_(self):
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡸࡴࠦࡢࡦࠢࡨࡼࡪࡩࡵࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤৰ")
        try:
            from browserstack_sdk.bstack11ll1l1l_opy_ import bstack11ll1111_opy_
            bstack111l1111_opy_ = bstack11ll1111_opy_(bstack11ll11l1_opy_=self.bstack1lllll111_opy_, bstack11ll11ll_opy_=True)
            if not bstack111l1111_opy_.get(bstack11l1l11_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬৱ"), False):
                self.logger.error(bstack11l1l11_opy_ (u"࡚ࠧࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠤ৲").format(bstack111l1111_opy_.get(bstack11l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ৳"), bstack11l1l11_opy_ (u"ࠧࡖࡰ࡮ࡲࡴࡽ࡮ࠡࡧࡵࡶࡴࡸࠧ৴"))))
                return []
            test_files = bstack111l1111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬ৵"), [])
            count = bstack111l1111_opy_.get(bstack11l1l11_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৶"), 0)
            self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡇࡴࡲ࡬ࡦࡥࡷࡩࡩࠦࡻࡾࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࢀࢃࠠࡧ࡫࡯ࡩࡸࠨ৷").format(count, len(test_files)))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦ৸").format(e))
            return []