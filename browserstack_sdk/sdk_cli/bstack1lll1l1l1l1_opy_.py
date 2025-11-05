# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lllllll11l_opy_,
    bstack1lll1l1lll1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll11l1lll_opy_, bstack11llll111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_, bstack1llll111111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l11_opy_ import bstack1lll1lll111_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1llll_opy_ import bstack1lll1llllll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1lll11111l_opy_ import bstack111111ll11_opy_, bstack1l1ll1l11l_opy_, bstack11ll1l1l1l_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll11l1_opy_(bstack1lll1llllll_opy_):
    bstack1lll1l1ll1l_opy_ = bstack1lll11l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥᄛ")
    bstack1lll11ll1l1_opy_ = bstack1lll11l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄜ")
    bstack1lll1l11l1l_opy_ = bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄝ")
    bstack1lll11lll1l_opy_ = bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄞ")
    bstack1lll11ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧᄟ")
    bstack1lll11l1ll1_opy_ = bstack1lll11l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣᄠ")
    bstack1lll1l1l1ll_opy_ = bstack1lll11l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᄡ")
    bstack1lll1ll1ll1_opy_ = bstack1lll11l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤᄢ")
    def __init__(self):
        super().__init__(bstack1lll1ll1111_opy_=self.bstack1lll1l1ll1l_opy_, frameworks=[bstack1llllll1ll1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.BEFORE_EACH, bstack1lll11lll11_opy_.POST), self.bstack1lll1l1l11l_opy_)
        if bstack11llll111l_opy_():
            TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1llll111l11_opy_)
        else:
            TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1llll11_opy_ = self.bstack1lll1lllll1_opy_(instance.context)
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡳࡥ࡬࡫࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᄣ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠨࠢᄤ"))
            return
        f.bstack1llll1ll11l_opy_(instance, bstack1lll1ll11l1_opy_.bstack1lll11ll1l1_opy_, bstack1lll1llll11_opy_)
    def bstack1lll1lllll1_opy_(self, context: bstack1lll1l1lll1_opy_, bstack1llll11111l_opy_= True):
        if bstack1llll11111l_opy_:
            bstack1lll1llll11_opy_ = self.bstack1lll1ll1lll_opy_(context, reverse=True)
        else:
            bstack1lll1llll11_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll1llll11_opy_ if f[1].state != bstack1111111111_opy_.QUIT]
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l11l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if not bstack1lll11l1lll_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄥ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠣࠤᄦ"))
            return
        bstack1lll1llll11_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄧ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᄨ"))
            return
        if len(bstack1lll1llll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄩ"))
        bstack1lll1l11ll1_opy_, bstack1lll11llll1_opy_ = bstack1lll1llll11_opy_[0]
        page = bstack1lll1l11ll1_opy_()
        if not page:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄪ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠨࠢᄫ"))
            return
        bstack1l1llll1l_opy_ = getattr(args[0], bstack1lll11l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᄬ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᄭ")).get(bstack1lll11l_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᄮ")):
            try:
                page.evaluate(bstack1lll11l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄯ"),
                            bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨᄰ") + json.dumps(
                                bstack1l1llll1l_opy_) + bstack1lll11l_opy_ (u"ࠧࢃࡽࠣᄱ"))
            except Exception as e:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦᄲ"), e)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l11l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if not bstack1lll11l1lll_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄳ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠣࠤᄴ"))
            return
        bstack1lll1llll11_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄵ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᄶ"))
            return
        if len(bstack1lll1llll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄷ"))
        bstack1lll1l11ll1_opy_, bstack1lll11llll1_opy_ = bstack1lll1llll11_opy_[0]
        page = bstack1lll1l11ll1_opy_()
        if not page:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄸ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠨࠢᄹ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1lll11l_opy_, None)
        if not status:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᄺ") + str(bstack1lllll1l111_opy_) + bstack1lll11l_opy_ (u"ࠣࠤᄻ"))
            return
        bstack1lll1l1ll11_opy_ = {bstack1lll11l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᄼ"): status.lower()}
        bstack1lll1lll1l1_opy_ = f.get_state(instance, TestFramework.bstack1lll11lllll_opy_, None)
        if status.lower() == bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᄽ") and bstack1lll1lll1l1_opy_ is not None:
            bstack1lll1l1ll11_opy_[bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᄾ")] = bstack1lll1lll1l1_opy_[0][bstack1lll11l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᄿ")][0] if isinstance(bstack1lll1lll1l1_opy_, list) else str(bstack1lll1lll1l1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᅀ")).get(bstack1lll11l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅁ")):
            try:
                page.evaluate(
                        bstack1lll11l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᅂ"),
                        bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࠧᅃ")
                        + json.dumps(bstack1lll1l1ll11_opy_)
                        + bstack1lll11l_opy_ (u"ࠥࢁࠧᅄ")
                    )
            except Exception as e:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠦᅅ"), e)
    def bstack1llll11l111_opy_(
        self,
        instance: bstack1llll111111_opy_,
        f: TestFramework,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l11l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if not bstack1lll11l1lll_opy_:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᅆ"))
            return
        bstack1lll1llll11_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅇ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠢࠣᅈ"))
            return
        if len(bstack1lll1llll11_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll1l11_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᅉ"))
        bstack1lll1l11ll1_opy_, bstack1lll11llll1_opy_ = bstack1lll1llll11_opy_[0]
        page = bstack1lll1l11ll1_opy_()
        if not page:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅊ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠥࠦᅋ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1lll11l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᅌ") + str(timestamp)
        try:
            page.evaluate(
                bstack1lll11l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᅍ"),
                bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᅎ").format(
                    json.dumps(
                        {
                            bstack1lll11l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅏ"): bstack1lll11l_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥᅐ"),
                            bstack1lll11l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅑ"): {
                                bstack1lll11l_opy_ (u"ࠥࡸࡾࡶࡥࠣᅒ"): bstack1lll11l_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣᅓ"),
                                bstack1lll11l_opy_ (u"ࠧࡪࡡࡵࡣࠥᅔ"): data,
                                bstack1lll11l_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧᅕ"): bstack1lll11l_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨᅖ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡴ࠷࠱ࡺࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡼࡿࠥᅗ"), e)
    def bstack1lll11ll111_opy_(
        self,
        instance: bstack1llll111111_opy_,
        f: TestFramework,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1l11l_opy_(f, instance, bstack1lllll1l111_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11l1ll1_opy_, False):
            return
        self.bstack1llllll1lll_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l111_opy_)
        req.test_framework_state = bstack1lllll1l111_opy_[0].name
        req.test_hook_state = bstack1lllll1l111_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11ll11l_opy_)
        for bstack1lll1l1111l_opy_ in bstack1lll1lll111_opy_.bstack1llll111ll1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1lll11l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣᅘ")
                if bstack1lll11l1lll_opy_
                else bstack1lll11l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤᅙ")
            )
            session.ref = bstack1lll1l1111l_opy_.ref()
            session.hub_url = bstack1lll1lll111_opy_.get_state(bstack1lll1l1111l_opy_, bstack1lll1lll111_opy_.bstack1llll111lll_opy_, bstack1lll11l_opy_ (u"ࠦࠧᅚ"))
            session.framework_name = bstack1lll1l1111l_opy_.framework_name
            session.framework_version = bstack1lll1l1111l_opy_.framework_version
            session.framework_session_id = bstack1lll1lll111_opy_.get_state(bstack1lll1l1111l_opy_, bstack1lll1lll111_opy_.bstack1llll111l1l_opy_, bstack1lll11l_opy_ (u"ࠧࠨᅛ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1llll11_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11ll1l1_opy_, [])
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅜ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠢࠣᅝ"))
            return
        if len(bstack1lll1llll11_opy_) > 1:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅞ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠤࠥᅟ"))
        bstack1lll1l11ll1_opy_, bstack1lll11llll1_opy_ = bstack1lll1llll11_opy_[0]
        page = bstack1lll1l11ll1_opy_()
        if not page:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅠ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠦࠧᅡ"))
            return
        return page
    def bstack1lll1ll1l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll1111ll_opy_ = {}
        for bstack1lll1l1111l_opy_ in bstack1lll1lll111_opy_.bstack1llll111ll1_opy_.values():
            caps = bstack1lll1lll111_opy_.get_state(bstack1lll1l1111l_opy_, bstack1lll1lll111_opy_.bstack1lll1llll1l_opy_, bstack1lll11l_opy_ (u"ࠧࠨᅢ"))
        bstack1llll1111ll_opy_[bstack1lll11l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦᅣ")] = caps.get(bstack1lll11l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣᅤ"), bstack1lll11l_opy_ (u"ࠣࠤᅥ"))
        bstack1llll1111ll_opy_[bstack1lll11l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᅦ")] = caps.get(bstack1lll11l_opy_ (u"ࠥࡳࡸࠨᅧ"), bstack1lll11l_opy_ (u"ࠦࠧᅨ"))
        bstack1llll1111ll_opy_[bstack1lll11l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᅩ")] = caps.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥᅪ"), bstack1lll11l_opy_ (u"ࠢࠣᅫ"))
        bstack1llll1111ll_opy_[bstack1lll11l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤᅬ")] = caps.get(bstack1lll11l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦᅭ"), bstack1lll11l_opy_ (u"ࠥࠦᅮ"))
        return bstack1llll1111ll_opy_
    def bstack1lll1ll111l_opy_(self, page: object, bstack1lll1l111l1_opy_, args={}):
        try:
            bstack1lll1l111ll_opy_ = bstack1lll11l_opy_ (u"ࠦࠧࠨࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫ࠲࠳࠴ࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠳ࡶࡵࡴࡪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢁࡦ࡯ࡡࡥࡳࡩࡿࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫࠫࡿࡦࡸࡧࡠ࡬ࡶࡳࡳࢃࠩࠣࠤࠥᅯ")
            bstack1lll1l111l1_opy_ = bstack1lll1l111l1_opy_.replace(bstack1lll11l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅰ"), bstack1lll11l_opy_ (u"ࠨࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸࠨᅱ"))
            script = bstack1lll1l111ll_opy_.format(fn_body=bstack1lll1l111l1_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠢࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡆࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷ࠰ࠥࠨᅲ") + str(e) + bstack1lll11l_opy_ (u"ࠣࠤᅳ"))