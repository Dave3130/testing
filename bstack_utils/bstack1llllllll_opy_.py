# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1llll1l_opy_
from bstack_utils.bstack111l1111_opy_ import bstack1llllll11_opy_
from bstack_utils.helper import bstack1ll11lll11_opy_
import json
class bstack1lll1l11l_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lll1l1_opy_ = bstack11ll1llll1l_opy_(self.config, logger)
        self.bstack111l1111_opy_ = bstack1llllll11_opy_.bstack111111ll_opy_(config=self.config)
        self.bstack11111llll11_opy_ = {}
        self.bstack111ll1ll_opy_ = False
        self.bstack11111lll11l_opy_ = (
            self.__11111lll111_opy_()
            and self.bstack111l1111_opy_ is not None
            and self.bstack111l1111_opy_.bstack1lll11l1l_opy_()
            and config.get(bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩệ"), None) is not None
            and config.get(bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨỈ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111111ll_opy_(cls, config, logger):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack1lll1l11l_opy_(config, logger)
        return cls._1ll1l1lll11_opy_
    def bstack1lll11l1l_opy_(self):
        bstack11ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡈࡴࠦ࡮ࡰࡶࠣࡥࡵࡶ࡬ࡺࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡺ࡬ࡪࡴ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏ࠲࠳ࡼࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡷࡪࡥࡳ࡫ࡱ࡫ࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤỉ")
        return self.bstack11111lll11l_opy_ and self.bstack11111lll1ll_opy_()
    def bstack11111lll1ll_opy_(self):
        bstack11111llll1l_opy_ = os.getenv(bstack11ll1l_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨỊ"), self.config.get(bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫị"), None))
        return bstack11111llll1l_opy_ in bstack11l11ll1l11_opy_
    def __11111lll111_opy_(self):
        bstack11ll11ll11l_opy_ = False
        for fw in bstack11l11llllll_opy_:
            if fw in self.config.get(bstack11ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬỌ"), bstack11ll1l_opy_ (u"ࠪࠫọ")):
                bstack11ll11ll11l_opy_ = True
        return bstack1ll11lll11_opy_(self.config.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨỎ"), bstack11ll11ll11l_opy_))
    def bstack11111ll1lll_opy_(self):
        return (not self.bstack1lll11l1l_opy_() and
                self.bstack111l1111_opy_ is not None and self.bstack111l1111_opy_.bstack1lll11l1l_opy_())
    def bstack11111ll1l1l_opy_(self):
        if not self.bstack11111ll1lll_opy_():
            return
        if self.config.get(bstack11ll1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪỏ"), None) is None or self.config.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩỐ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11ll1l_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥࡵࡲࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡱࡹࡱࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡸࠥࡧࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥ࠯ࠤố"))
        if not self.__11111lll111_opy_():
            self.logger.info(bstack11ll1l_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡨࡲࡦࡨ࡬ࡦࠢ࡬ࡸࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠲ࠧỒ"))
    def bstack11111ll1ll1_opy_(self):
        return self.bstack111ll1ll_opy_
    def bstack111l1lll_opy_(self, bstack11111lllll1_opy_):
        self.bstack111ll1ll_opy_ = bstack11111lllll1_opy_
        self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠥồ"), bstack11111lllll1_opy_)
    def bstack1111111l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡲࡶࡩ࡫ࡲࡪࡰࡪ࠲ࠧỔ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack111l1111_opy_.bstack111lll11111_opy_()
            if self.bstack111l1111_opy_ is not None:
                orchestration_strategy = self.bstack111l1111_opy_.bstack1l1lllll1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11ll1l_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦࡩࡴࠢࡑࡳࡳ࡫࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡵࡳࡨ࡫ࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴ࠢổ"))
                return None
            self.logger.info(bstack11ll1l_opy_ (u"ࠧࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥỖ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡉࡌࡊࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤỗ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡳࡥ࡭ࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥỘ"))
                self.bstack11111lll1l1_opy_.bstack11ll1llllll_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lll1l1_opy_.bstack11ll1l11lll_opy_()
            if not ordered_test_files:
                return None
            self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥộ"), len(test_files))
            self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧỚ"), int(os.environ.get(bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨớ")) or bstack11ll1l_opy_ (u"ࠦ࠵ࠨỜ")))
            self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤờ"), int(os.environ.get(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤỞ")) or bstack11ll1l_opy_ (u"ࠢ࠲ࠤở")))
            self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧỠ"), len(ordered_test_files))
            self.bstack11111lll_opy_(bstack11ll1l_opy_ (u"ࠤࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡇࡐࡊࡅࡤࡰࡱࡉ࡯ࡶࡰࡷࠦỡ"), self.bstack11111lll1l1_opy_.bstack11ll1ll1ll1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡬ࡢࡵࡶࡩࡸࡀࠠࡼࡿࠥỢ").format(e))
        return None
    def bstack11111lll_opy_(self, key, value):
        self.bstack11111llll11_opy_[key] = value
    def bstack111l11lll_opy_(self):
        return self.bstack11111llll11_opy_