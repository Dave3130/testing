# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lllll11_opy_, bstack111l1ll1ll1_opy_
from bstack_utils.bstack1l11111lll_opy_ import bstack11l111ll11l_opy_
class bstack11lll1ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111ll1ll_opy_=None, bstack111111l1l1l_opy_=True, bstack1ll11l1ll11_opy_=None, bstack1111l11ll_opy_=None, result=None, duration=None, bstack1l1lll1l_opy_=None, meta={}):
        self.bstack1l1lll1l_opy_ = bstack1l1lll1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l1l1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111ll1ll_opy_ = bstack111111ll1ll_opy_
        self.bstack1ll11l1ll11_opy_ = bstack1ll11l1ll11_opy_
        self.bstack1111l11ll_opy_ = bstack1111l11ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1lll1l11_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11l11_opy_(self, meta):
        self.meta = meta
    def bstack111llll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111ll111_opy_(self):
        bstack111111lll1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ἅ"): bstack111111lll1l_opy_,
            bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ἆ"): bstack111111lll1l_opy_,
            bstack111l1l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪἇ"): bstack111111lll1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111l1l_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢἈ") + key)
            setattr(self, key, val)
    def bstack111111ll1l1_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἉ"): self.name,
            bstack111l1l_opy_ (u"ࠨࡤࡲࡨࡾ࠭Ἂ"): {
                bstack111l1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧἋ"): bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪἌ"),
                bstack111l1l_opy_ (u"ࠫࡨࡵࡤࡦࠩἍ"): self.code
            },
            bstack111l1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬἎ"): self.scope,
            bstack111l1l_opy_ (u"࠭ࡴࡢࡩࡶࠫἏ"): self.tags,
            bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪἐ"): self.framework,
            bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἑ"): self.started_at
        }
    def bstack111111ll11l_opy_(self):
        return {
         bstack111l1l_opy_ (u"ࠩࡰࡩࡹࡧࠧἒ"): self.meta
        }
    def bstack111111l11l1_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭ἓ"): {
                bstack111l1l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨἔ"): self.bstack111111ll1ll_opy_
            }
        }
    def bstack111111l1lll_opy_(self, bstack111111lll11_opy_, details):
        step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨἕ")] == bstack111111lll11_opy_, self.meta[bstack111l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ἖")]), None)
        step.update(details)
    def bstack11l111l1_opy_(self, bstack111111lll11_opy_):
        step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠧࡪࡦࠪ἗")] == bstack111111lll11_opy_, self.meta[bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἘ")]), None)
        step.update({
            bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ἑ"): bstack1lllll11_opy_()
        })
    def bstack1lll1lll_opy_(self, bstack111111lll11_opy_, result, duration=None):
        bstack1ll11l1ll11_opy_ = bstack1lllll11_opy_()
        if bstack111111lll11_opy_ is not None and self.meta.get(bstack111l1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἚ")):
            step = next(filter(lambda st: st[bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧἛ")] == bstack111111lll11_opy_, self.meta[bstack111l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἜ")]), None)
            step.update({
                bstack111l1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἝ"): bstack1ll11l1ll11_opy_,
                bstack111l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ἞"): duration if duration else bstack111l1ll1ll1_opy_(step[bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ἟")], bstack1ll11l1ll11_opy_),
                bstack111l1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἠ"): result.result,
                bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἡ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111lll1_opy_):
        if self.meta.get(bstack111l1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἢ")):
            self.meta[bstack111l1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἣ")].append(bstack1111111lll1_opy_)
        else:
            self.meta[bstack111l1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἤ")] = [ bstack1111111lll1_opy_ ]
    def bstack111111l11ll_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἥ"): self.bstack1lll1l11_opy_(),
            **self.bstack111111ll1l1_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack1111111llll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111l1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ἦ"): self.bstack1ll11l1ll11_opy_,
            bstack111l1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪἧ"): self.duration,
            bstack111l1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἨ"): self.result.result
        }
        if data[bstack111l1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἩ")] == bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬἪ"):
            data[bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬἫ")] = self.result.bstack1111111l1l_opy_()
            data[bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨἬ")] = [{bstack111l1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫἭ"): self.result.bstack1111ll1l1ll_opy_()}]
        return data
    def bstack111111l1ll1_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧἮ"): self.bstack1lll1l11_opy_(),
            **self.bstack111111ll1l1_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack1111111llll_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack11llll11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111l1l_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫἯ") in event:
            return self.bstack111111l11ll_opy_()
        elif bstack111l1l_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ἰ") in event:
            return self.bstack111111l1ll1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll11l1ll11_opy_ = time if time else bstack1lllll11_opy_()
        self.duration = duration if duration else bstack111l1ll1ll1_opy_(self.started_at, self.bstack1ll11l1ll11_opy_)
        if result:
            self.result = result
class bstack1l1l1ll1_opy_(bstack11lll1ll_opy_):
    def __init__(self, hooks=[], bstack1llll11l_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1llll11l_opy_ = bstack1llll11l_opy_
        super().__init__(*args, **kwargs, bstack1111l11ll_opy_=bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࠪἱ"))
    @classmethod
    def bstack111111l1111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111l1l_opy_ (u"࠭ࡩࡥࠩἲ"): id(step),
                bstack111l1l_opy_ (u"ࠧࡵࡧࡻࡸࠬἳ"): step.name,
                bstack111l1l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩἴ"): step.keyword,
            })
        return bstack1l1l1ll1_opy_(
            **kwargs,
            meta={
                bstack111l1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪἵ"): {
                    bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨἶ"): feature.name,
                    bstack111l1l_opy_ (u"ࠫࡵࡧࡴࡩࠩἷ"): feature.filename,
                    bstack111l1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪἸ"): feature.description
                },
                bstack111l1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨἹ"): {
                    bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἺ"): scenario.name
                },
                bstack111l1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἻ"): steps,
                bstack111l1l_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫἼ"): bstack11l111ll11l_opy_(test)
            }
        )
    def bstack111111l111l_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩἽ"): self.hooks
        }
    def bstack111111l1l11_opy_(self):
        if self.bstack1llll11l_opy_:
            return {
                bstack111l1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪἾ"): self.bstack1llll11l_opy_
            }
        return {}
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            **self.bstack111111l1l11_opy_()
        }
    def event_key(self):
        return bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧἿ")
class bstack1l1lllll_opy_(bstack11lll1ll_opy_):
    def __init__(self, hook_type, *args,bstack1llll11l_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l1l11l_opy_ = None
        self.bstack1llll11l_opy_ = bstack1llll11l_opy_
        super().__init__(*args, **kwargs, bstack1111l11ll_opy_=bstack111l1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫὀ"))
    def bstack11llll1l_opy_(self):
        return self.hook_type
    def bstack111111llll1_opy_(self):
        return {
            bstack111l1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪὁ"): self.hook_type
        }
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭ὂ"): self.bstack1l111l1l11l_opy_,
            **self.bstack111111llll1_opy_()
        }
    def event_key(self):
        return bstack111l1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫὃ")
    def bstack11l11lll_opy_(self, bstack1l111l1l11l_opy_):
        self.bstack1l111l1l11l_opy_ = bstack1l111l1l11l_opy_