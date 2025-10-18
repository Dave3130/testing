# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1lll1l1_opy_ import bstack11ll1ll111l_opy_
from bstack_utils.bstack11l111l1_opy_ import bstack1111llll_opy_
from bstack_utils.helper import bstack111ll11ll_opy_
import json
class bstack111l1lll_opy_:
    _1ll1ll1l1l1_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l11l111_opy_ = bstack11ll1ll111l_opy_(self.config, logger)
        self.bstack11l111l1_opy_ = bstack1111llll_opy_.bstack11l11l1l_opy_(config=self.config)
        self.bstack1111l11l1l1_opy_ = {}
        self.bstack1llll111l_opy_ = False
        self.bstack1111l1111ll_opy_ = (
            self.__1111l11111l_opy_()
            and self.bstack11l111l1_opy_ is not None
            and self.bstack11l111l1_opy_.bstack1llll11l1_opy_()
            and config.get(bstack1l1lll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧẆ"), None) is not None
            and config.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ẇ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack11l11l1l_opy_(cls, config, logger):
        if cls._1ll1ll1l1l1_opy_ is None and config is not None:
            cls._1ll1ll1l1l1_opy_ = bstack111l1lll_opy_(config, logger)
        return cls._1ll1ll1l1l1_opy_
    def bstack1llll11l1_opy_(self):
        bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡆࡲࠤࡳࡵࡴࠡࡣࡳࡴࡱࡿࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡸࡪࡨࡲ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔ࠷࠱ࡺࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑࡵࡨࡪࡸࡩ࡯ࡩࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢẈ")
        return self.bstack1111l1111ll_opy_ and self.bstack1111l11l11l_opy_()
    def bstack1111l11l11l_opy_(self):
        bstack1111l111lll_opy_ = os.getenv(bstack1l1lll1_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ẉ"), self.config.get(bstack1l1lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩẊ"), None))
        return bstack1111l111lll_opy_ in bstack11l1l111l11_opy_
    def __1111l11111l_opy_(self):
        bstack11ll1l11l1l_opy_ = False
        for fw in bstack11l1l111ll1_opy_:
            if fw in self.config.get(bstack1l1lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪẋ"), bstack1l1lll1_opy_ (u"ࠨࠩẌ")):
                bstack11ll1l11l1l_opy_ = True
        return bstack111ll11ll_opy_(self.config.get(bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ẍ"), bstack11ll1l11l1l_opy_))
    def bstack1111l111l1l_opy_(self):
        return (not self.bstack1llll11l1_opy_() and
                self.bstack11l111l1_opy_ is not None and self.bstack11l111l1_opy_.bstack1llll11l1_opy_())
    def bstack1111l1111l1_opy_(self):
        if not self.bstack1111l111l1l_opy_():
            return
        if self.config.get(bstack1l1lll1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨẎ"), None) is None or self.config.get(bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧẏ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1l1lll1_opy_ (u"࡚ࠧࡥࡴࡶࠣࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡤࡣࡱࠫࡹࠦࡷࡰࡴ࡮ࠤࡦࡹࠠࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠣࡳࡷࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠ࡯ࡷ࡯ࡰ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡳࡦࡶࠣࡥࠥࡴ࡯࡯࠯ࡱࡹࡱࡲࠠࡷࡣ࡯ࡹࡪ࠴ࠢẐ"))
        if not self.__1111l11111l_opy_():
            self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡔࡦࡵࡷࠤࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡥࡤࡲࠬࡺࠠࡸࡱࡵ࡯ࠥࡧࡳࠡࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡦࡰࡤࡦࡱ࡫ࠠࡪࡶࠣࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠤ࡫࡯࡬ࡦ࠰ࠥẑ"))
    def bstack1111l111l11_opy_(self):
        return self.bstack1llll111l_opy_
    def bstack111lllll_opy_(self, bstack1111l111ll1_opy_):
        self.bstack1llll111l_opy_ = bstack1111l111ll1_opy_
        self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠣẒ"), bstack1111l111ll1_opy_)
    def bstack11l1l11l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠣ࡝ࡵࡩࡴࡸࡤࡦࡴࡢࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹ࡝ࠡࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡰࡴࡧࡩࡷ࡯࡮ࡨ࠰ࠥẓ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack11l111l1_opy_.bstack11l1111ll11_opy_()
            if self.bstack11l111l1_opy_ is not None:
                orchestration_strategy = self.bstack11l111l1_opy_.bstack1ll1ll111l_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤ࡮ࡹࠠࡏࡱࡱࡩ࠳ࠦࡃࡢࡰࡱࡳࡹࠦࡰࡳࡱࡦࡩࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠲ࠧẔ"))
                return None
            self.logger.info(bstack1l1lll1_opy_ (u"ࠥࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡼ࡯ࡴࡩࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࢁࡽࠣẕ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1l1lll1_opy_ (u"࡚ࠦࡹࡩ࡯ࡩࠣࡇࡑࡏࠠࡧ࡮ࡲࡻࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢẖ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1l1lll1_opy_ (u"࡛ࠧࡳࡪࡰࡪࠤࡸࡪ࡫ࠡࡨ࡯ࡳࡼࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣẗ"))
                self.bstack1111l11l111_opy_.bstack11lll111l11_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack1111l11l111_opy_.bstack11ll1lllll1_opy_()
            if not ordered_test_files:
                return None
            self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡆࡳࡺࡴࡴࠣẘ"), len(test_files))
            self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥẙ"), int(os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦẚ")) or bstack1l1lll1_opy_ (u"ࠤ࠳ࠦẛ")))
            self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢẜ"), int(os.environ.get(bstack1l1lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢẝ")) or bstack1l1lll1_opy_ (u"ࠧ࠷ࠢẞ")))
            self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠨࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥẟ"), len(ordered_test_files))
            self.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠢࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡅࡕࡏࡃࡢ࡮࡯ࡇࡴࡻ࡮ࡵࠤẠ"), self.bstack1111l11l111_opy_.bstack11lll11l1ll_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣ࡝ࡵࡩࡴࡸࡤࡦࡴࡢࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹ࡝ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡱࡧࡳࡴࡧࡶ࠾ࠥࢁࡽࠣạ").format(e))
        return None
    def bstack11l1l111_opy_(self, key, value):
        self.bstack1111l11l1l1_opy_[key] = value
    def bstack1ll1ll1l1l_opy_(self):
        return self.bstack1111l11l1l1_opy_